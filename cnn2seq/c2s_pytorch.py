from copy import deepcopy
import pandas
import pickle
import numpy as np
import random
import os
import sys
util_path = os.path.abspath(os.path.join('../util'))
sys.path.append(util_path)
import set_assembler
import torch
from time import sleep

from torch.autograd import Variable
from torch.nn import init
import torch.nn.functional as F

# TODO: Replace magic constant in cnn._lin

def alph2vec_vec2alph_from_alph(alphabet):
    vec = pandas.get_dummies(sorted(list(alph))).to_dict()
    for k in vec.keys():
        vs = vec[k].values()
        vec[k] = tuple([v for v in vs])
    a2v = vec
    v2a = {value:key for key,value in a2v.items()}
    return a2v, v2a

def str_to_one_hots(s, l_alph, a2v):
    l = len(s)
    one_hots = np.zeros([l, l_alph])
    seq_pos = 0
    for c in s:
        one_hots[seq_pos] = a2v[c]
        seq_pos += 1
    return list(one_hots)

def one_hot_to_idx(v):
    for i in range(v.shape[0]):
        if v[i] == 1.:
            return i
    return -1.

class CNN(object):
    def __init__(self, in_shape, out_shape, activation, layer_params, channels):
        """ Constructs a Convolutional Neural Network (CNN).

            Args:
                in_shape: Shape of the 2-dimensional network input.
                out_shape: Shape of the network's output flattened,
                    fully-connected layer.
                activation: The activation function to apply to each
                    convolutional layer. Should be a torch.nn.functional method.
                layer_params: List of dictionaries specifying the consecutive
                    layers of the CNN. Each dictionary should specify
                    the following fields:
                        -'type': Type of layer to construct.
                            e.g. 'conv', 'max_pool'
                        -'kernel': Size of the layer's sliding window.
                        -'strides': Stride of the convolving kernel.
                            Can be a 2D tuple (height, width) or a single
                            integer.
                        -'padding': Integer (0 or 1). Whether or not to apply
                            zero padding to the layer's input.
                        -'out_channels': 'conv'-layer only. The number of
                            channels in the layer's output.
        """
        assert(len([l for l in layer_params if l['type'] == 'conv']) == len(channels))

        act2str = {F.elu: 'elu',
                   F.relu: 'relu'}

        self.in_shape = in_shape
        self.out_shape = out_shape
        self.last_channels = self.in_shape[1]
        self.act_str = act2str[activation]
        self._cnn = torch.nn.ModuleList()

        for ps in layer_params:
            if ps['type'] == 'conv':
                self.add_conv_layer(ps)
            elif ps['type'] == 'max_pool':
                self.add_max_pool(ps)
            else:
                raise TypeError("Unsupported CNN layer type.")
        self._cnn = self._cnn.cuda()
        self._lin = torch.nn.Linear(73728, self.out_shape).cuda()

    def add_conv_layer(self, ps):
        in_channels = self.last_channels
        out_channels = ps['channels']
        kernel = ps['kernel']
        strides = ps['strides']
        padding = ps['padding']
        new_layer = torch.nn.Conv2d(in_channels, out_channels, kernel,
                         stride=strides, padding=padding)
        torch.nn.init.xavier_uniform(new_layer.weight,
                                     gain=torch.nn.init.calculate_gain(self.act_str))
        self._cnn.append(new_layer)
        self.last_channels = out_channels

    def add_max_pool(self, ps):
        kernel = ps['kernel']
        strides = ps['strides']
        padding = ps['padding']
        new_layer = torch.nn.MaxPool2d(kernel, stride=strides, padding=padding)
        self._cnn.append(new_layer)

    def forward(self, x):
        for l in self._cnn:
            x = l(x)
        out_shape = x.size()
        new_shape = [1, out_shape[1] * out_shape[2] * out_shape[3]]
        x = x.view(new_shape)
        x = self._lin(x)
        return x

class RNN(object):
    def __init__(self, in_shape, hidden_shape, cell_shape, batch_size,
                 alphabet_length, cnn):
        self.batch_size = batch_size
        self.in_shape = in_shape
        self.h_shape = hidden_shape
        self.c_shape = cell_shape
        self._rnn = torch.nn.ModuleList()
        self._rnn.append(torch.nn.LSTM(self.in_shape, self.h_shape))
        self._rnn.append(torch.nn.Linear(self.h_shape, alphabet_length))
        self._rnn.append(torch.nn.Softmax())
        self._rnn = self._rnn.cuda()

        self.h0 = Variable(torch.zeros(1, self.batch_size, hidden_shape)).cuda()
        self.c0 = Variable(torch.zeros(1, self.batch_size, cell_shape)).cuda()
        self.hidden0 = (self.h0, self.c0)
        self.h = Variable(torch.randn(1, self.batch_size, hidden_shape)).cuda()
        self.c = Variable(torch.randn( self.batch_size, cell_shape)).cuda()
        self.hidden = (self.h, self.c)

    def forward(self, x, hidden):
        x = x.view([1, 1, self.in_shape])
        # print(x.size())
        x, hidden = self._rnn[0](x, hidden)
        x2 = x.view([1, x.size()[-1]])
        x2 = self._rnn[1](x2)
        x2 = self._rnn[2](x2)
        return x, x2, hidden

    def process_sample_(self, x, y, l_alph, a2v, v2a, null_char="#"):
        y += null_char
        pred = Variable(torch.FloatTensor(len(y), l_alph))
        h_c = self.hidden0
        l_o = 0
        l_y = len(y)
        oh_y = str_to_one_hots(y, l_alph, a2v)
        char_output = None
        output_str = ""
        while char_output is not null_char and l_o < l_y:
            x, x2, h_c = self.forward(x, h_c)
            top, idx = torch.topk(x2, 1)
            alph_size = torch.Size([l_alph])
            oh = torch.sparse.FloatTensor(idx.data, torch.FloatTensor([1.]),
                                          alph_size).to_dense()
            char_output = v2a[tuple(oh.numpy())]
            output_str += char_output
            pred[l_o] = x2.data
            l_o += 1
        target = torch.from_numpy(np.asarray(oh_y)).long()
        target = target.view([l_y * l_alph])

class C2S(object):
    def __init__(self, in_shape, cnn_out_shape, rnn_hidden_shape, alphabet,
               cnn_activation, cnn_params, cnn_channels):
        self.l_alph = len(alphabet)
        self._cnn = CNN(in_shape, cnn_out_shape, cnn_activation, cnn_params,
                        cnn_channels)
        self._rnn = RNN(cnn_out_shape, rnn_hidden_shape, rnn_hidden_shape, 1,
                        self.l_alph, self._cnn)
        self.a2v, self.v2a = alph2vec_vec2alph_from_alph(alphabet)

    def forward(self, x, y, null_char="#"):
        x = Variable(torch.from_numpy(x).float()).cuda()
        x = x.view([1] + [1] + list(x.size())[:-1])
        x = self._cnn.forward(x)

        y += null_char
        l_y = len(y)
        l_o = 0
        char_output = None
        hidden = self._rnn.hidden0

        loss = 0.
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(list(self._rnn._rnn.parameters()) + \
                                     list(self._cnn._cnn.parameters()) + \
                                     list(self._cnn._lin.parameters()), lr=5e-4)
        print(y)
        result = ""
        # while char_output is not null_char and l_o < l_y:
        while l_o < l_y:
            x, x2, hidden = self._rnn.forward(x, hidden)
            y_np = a2v[y[l_o]]
            top, idx = torch.topk(x2, 1)
            oh = torch.sparse.FloatTensor(idx.data.cpu(), torch.FloatTensor([1.]),
                                          torch.Size([self.l_alph])).to_dense()
            char_output = v2a[tuple(oh.numpy())]
            y_o_oh = np.asarray(a2v[y[l_o]])
            y_o_oh = one_hot_to_idx(y_o_oh)
            y_o_oh = Variable(torch.LongTensor([y_o_oh]))
            # print(y_o_oh)
            # print("\'" + char_output + "\'")
            loss += criterion(x2.view([1, self.l_alph]), y_o_oh.cuda())
            loss.backward(retain_variables=True)
            l_o += 1
            result += char_output
            print(result, end="\r")
            # print("\n" + str(loss.data.numpy()))
            optimizer.step()
            optimizer.zero_grad()
            loss = 0.
        print()

if __name__ == '__main__':
    # Data initialization
    # TODO: Refactor into own module
    null_char = "#"
    train_path = "../mol2/ai.db"
    train_directory = "../mol2/im/"
    test_path = "../mol/ai.db"
    test_directory = "../mol/im/"
    table_name = "AI"
    train_n_noise_variants = 6
    img_base = "noise"
    img_extension = ".png"

    rows = set_assembler.fetch_rows(train_path, table_name)
    train_alphabet = str(set_assembler.alph_from_rows(rows))
    train_alphabet += null_char
    train_seq_len = set_assembler.seq_len_from_rows(rows)
    train_set = set_assembler.cross_reference_db_imgs(rows, train_directory,
                    train_n_noise_variants, img_extension, img_base)
    img = train_set[0][0]
    resolution = (len(img[0]), len(img[1]))

    rows = set_assembler.fetch_rows(test_path, table_name)
    test_alphabet = str(set_assembler.alph_from_rows(rows)) + null_char

    alph = set(train_alphabet + test_alphabet)
    l_alph = len(alph)
    a2v, v2a = alph2vec_vec2alph_from_alph(alph)

    batch_size = 1
    # batch_size x in_channels x h x w
    cnn_in_shape = [batch_size] + [1] + list(resolution)
    rnn_shape = 1024
    cnn_out_shape = rnn_shape
    rnn_h = rnn_shape
    rnn_c = rnn_shape

    cnn_activation = F.relu
    conv_dict = {'type': 'conv',
                 'kernel': 3,
                 'strides': 1,
                 'padding': 1}
    pool = {'type': 'max_pool',
                 'kernel': 2,
                 'strides': 2,
                 'padding': 0}
    chans = [64]*2 + [256]*2 + [512]*2
    chans_counter = 0
    cnn_ps = []
    convs_per_pool = 2
    n_superlayers = 3
    for i in range(n_superlayers):
        for j in range(convs_per_pool):
            d = deepcopy(conv_dict)
            d['channels'] = chans[chans_counter]
            chans_counter += 1
            cnn_ps.append(d)
        cnn_ps.append(pool)

    x = img
    y = train_set[0][1].decode('ascii')

    c2s = C2S(cnn_in_shape, cnn_out_shape, rnn_h, alph,
              cnn_activation, cnn_ps, chans)
    for i in range(10000):
        print("****" + str(i) + "****")
        c2s.forward(x, y)

        # print('\n****************')
    # x = Variable(torch.randn(cnn_in_shape))
    # print("Initializing CNN...")
    # cnn = CNN(cnn_in_shape, cnn_out_shape, cnn_activation, cnn_ps, chans)
    # print("Done!\nInitializing RNN...")
    # rnn = RNN(cnn_out_shape, rnn_h, rnn_c, batch_size, l_alph, cnn._cnn)
    # print("Done!")
    # print("Dummy input test...")
    # rnn.process_sample(cnn.forward(x)[0], y, l_alph, a2v, v2a)

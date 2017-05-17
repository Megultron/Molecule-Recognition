# ssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssyyyyssyyyyssyyysssssssssssssssyyyyyyyd
# ssysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysyyyyysssssssssssssssyyyyyyyyym
# yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhddmmmmmmmddmmdhyyyyysyysssssssssssyyyyyyyyyhm
# ysysyyyyyyyyyyyyyyyyyyyyyyyyhmmNNNNNNNNNNNNNNNNNmmhyyyyssysssssyyyyyyyyyyyyydN
# ssyysyyyyyyyyyyyyyyyyyyyyyohNNNNNNNNNNNNNNNNNNNNNNNmmhyyssssssyyyysyyyyyyyyhmN
# ysyyyyyyyyyyyyyyyyyyhddyo/yNNNNNNNNNNNNNNNNNNNNNNNNNNNmdysyysyyyyysyyyyyyyydNN
# yyyyyyyyyyyyyyyyyyyhddmmNdmNNNNNNNNNNdsdmmmmNNNNNNNNNNNmdhyyyyyyyysyyyyyyyhmNN
# yyyyyyyyyyyhdhhhhdhmdmdsmdNNNNNNNNNNm+/dmhshmmmNNNNNNNNNmmdyyyyyyyyyyyyyyyhmNN
# yyyyyyyyyhdhyyyyyhmNmhdsmmNNNNNNNNNNNmmmd:.-ymmNNNNNNmdyssyyyyyyyyyyyyyyyhdNNN
# yyyyyyyhdhyyyyyyyhNms.:hmNNNNNNNNNNNNNNNmdhhmmNNNNds+:.....-+hyyyyyyyyhhyhmNNN
# yyyyyyhdyyyyyyyyyydmhohddMNNNNMNNNNNNNNNNNNNNNNmys/::-.......yhhhyyyhhhhhdNNNN
# yyyyyymyyyyyyyyyyyhdmmdsmMMNNNMMNNNNNNNNNNNNNms+//+hhhs+-....+yhhyyyhhhhhmNNNN
# yyyyyhmyyyyyyyyyyyhyhyssmMMMMMMMMMMMMNNNNNNNdsssyhsydyhsy-...:oyhhyyhhhhdNNNNN
# yyyyyhmyyyyyyyyyyyyhsssymMMMMMMMMMMMMMMNMMNhyhsdsdmoosdso--+os/+yhyyhhhhmNNNNN
# yyyyyymhyyyyyyyyyyhyhyyydNMMMMMMMMMMMMMMNNhohsd/-/+-/sms.:hmd/:/shyyhhhdmNNNNN
# yyyyyyhmyyyyyyyyyydyyhyyydMMMNmmMMMMMMMNmyo+yy++-///+dm//hmm+:oysyyyhhhmNNNNNN
# yyyyyyyhddyyyyyyyyhmhhhhyydmMNmdNMMMMMNhso++oho+ooo++y/:ymmh+odd+shyhhhmNNNNNN
# yyyyyyyyyhddhhyyyyyhdhhhyssshmmNNNNmmdyso++//+so///::::oydmhshdhyyyyyydmmmNNNN
# yyyyyyyyyyyyhhddhyyydmdhhhysooosyyyyssssoo+//////::://++sdNhyysssssssymNNmdNNm
# yyyyyyyyyyyyyyyhmhyyyhddhhhyyyyso+++++++++++//////oo+++oshdossssssooshmNNNmdmm
# yyyyyyyyyyyyyyyyhmyyyyyhdddhhhhyyyysssooooooo+++++++ooosdy++++/////+oyyyyydhyh
# yyyyyyyyyyyyyyyyhmyyyyyyyhdddddhhyyyyyyyysssoooooooooohds///////++/::/++/oh+//
# yyyyyyyyyyyyyyyyymhyyyyyyyyhdddddddddhhhhhhhyyyyso+oyhs+////+++/:-..-/+osy+///
# yyyyyyyyyyyyyyyyyddyyyyyyyyyyhddmdddddddddhyyhhyhyys+////+++/::++ooosyso+//:::
# yyyyyyyyyyyyyyyyyyhddhmNmddmmmNNMMNNNNmmmmmmmmhs+/:-//++/:--:so/:---://:::::::
# yyyyyyyyyyyyyyyyyyyyhdMMNNNMMMMNNMMMMMMMMMMMMNmdho::+/:--../y:.....-::::::::-:
# hhyyyyyyysssosssssyyhhNNNNNMNNmhsMMMMMMMMMNMMMMNNNmhdo:--:/y:......::::::--://
# mdhhyysssosssyyyhhhhhdddddmdhddmdNNNNNNNNNNNNNNNNNNmmhss+++:......-:::--://///
# dhyysysyyyyyyyhhhhhhhhdddhyhdmmmdddddddddhyyssoo+//:::/:::+/+o+/:-:-----://///
# ysyyyyhhhyyyyyhhhhhhhhhysydmddhhhhhhhhhyyyssooo+/::/:::...---//syhs::-.--/////
# hyhhhhhhhhyyyyhhhhhhhhsohmdhhyyyysssssssssooooo+++o/:---......--:/hd/o/--:////
# ddddddhhhhhhhhhhhhyyhyyddhhyyyssoooo++oooooooo+++++o+::----....--:oy:+ds/+/://
# mmddddhhhhhhhyyhyhdyhdmdhyyyyssoo+o+ooooooooooshhhs/:---:--...--:/oyhdNmmNdy+/
# mmdhhhhhhhhhhyyyhdyyhmdhyssoo+++/+++++ooossssdmy+/:-..`.::::::-:+yddNNNNNNMMNd
# yyhhhhhhhyhhhhydmhydNmhyyssoo+///::::/++ossohdo///:--....::///+oo++dNNNNNNNNNN
# hhyssyyyyyyhdyhmhydmdhysssoo+++++ooooossyhhyhso++//::-....+++//+osdMMNNMMMMNMM
# yyyyyysssyhhhydmyymdhyssssooo+++oo+oosyyhdmNhyssoo+//:-....shmNNmmdNMNNMMMMMMN
# yyyyyyyyysssssyyssyssooo++oooossssyyyyyhhddmmhhyysoo+/:--..+NMNNdhhhMMNNNNMMMM
# mhhyssssyyysyssyysssssssssssssssssssssssyyhmmNNmhhysoo+ooo+/oNNNNhoosNMNNNMMMM
# MMMMMNmdhyso+ooooooooooooooosssyyhddmNNMMMMMMMMMMNdhyyhyyo+oosdmmdh:-/NNNNMMMM
# MMMMMMMMMMMMNmdhyyyhdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhyhysssosyhh/:+MMMMMMM
# MMMMMMMMMMMMMMMMMMMNmdysymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdmdhyyssyhhyyo+NMMMMMM
# MMMMMMMMMMMMMMMMMMMMMMmhhdyhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdmdhhhdhysssssydmNMM
# MMMMMMMMMMMMMMMMMMMMMMMMMMMmyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMNmmmhyyyssssyhhyy
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMdsNMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMmhhhyyyhhysso

import cPickle as pickle
import numpy as np
import pandas
import random
import tensorflow as tf
import tensorflow.contrib.slim as slim
import os
import sys
util_path = os.path.abspath(os.path.join('..'))
sys.path.append(util_path)

sess = tf.Session()

def variable_summaries(var, name):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.scalar_summary('mean/' + name, mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.scalar_summary('stddev/' + name, stddev)
        tf.scalar_summary('max/' + name, tf.reduce_max(var))
        tf.scalar_summary('min/' + name, tf.reduce_min(var))
        tf.histogram_summary(name, var)

def calc_max_one_hot(vec):
    max_element = np.amax(np.array(vec))
    for i in range(len(vec)):
        vec[i] = 1.0 if vec[i] == max_element else 0.0
    return vec

def convert_to_one_hot(val, target_len):
    val = int(val)
    one_hot = np.zeros(target_len)
    one_hot[val] = 1.0
    return one_hot


class ConvNet(object):
    def __init__(self, resolution, conv_shapes, fc_shapes, filter_shapes,   stride_shapes, batch_size):
        """Constructs a tensorflow convolutional neural network.

            Args:
                resolution: Numpy array of iput image resolution.
                conv_shapes: List of convolutional layer sizes.
                fc_shapes: List of fully connected layer sizes.
                filter_shapes: Numpy array of 2D filter (or kernel) dimensions.
                stride_shapes: Numpy array of 2d stride dimensions.

            Returns:
                N/A

            Raises:
                AssertionError: The number of convolution layer, filter, and
                    stride shapes are not equal.
        """
        assert len(conv_shapes) == len(filter_shapes) == len(stride_shapes)

        self.resolution = resolution
        self.inputs = tf.placeholder(tf.float32, [batch_size] + \
                        list(resolution) + [1], name="Input")
        self.output_shape = fc_shapes[-1]

        # variable_summaries(self.inputs, self.inputs.name)

        self.layers = []
        with tf.name_scope('cnn_layers') as scope:
            # construct convolutional layers
            tmp_conv = tf.contrib.layers.convolution2d(self.inputs,
                        num_outputs=conv_shapes[0], kernel_size=filter_shapes[0],
                        stride=stride_shapes[0], activation_fn=tf.nn.relu,
                        weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                        biases_initializer=tf.constant_initializer(0.1),
                        scope='conv_1')
            self.layers.append(tmp_conv)

            for i in range(1, len(conv_shapes)):
                layer_label = "conv_" + str(i+1)
                tmp_conv = tf.contrib.layers.convolution2d(self.layers[-1],
                            num_outputs=conv_shapes[i], kernel_size=filter_shapes[i],
                            stride=stride_shapes[i], activation_fn=tf.nn.relu,
                            weights_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                            biases_initializer=tf.constant_initializer(0.1),
                            scope=layer_label)
                self.layers.append(tmp_conv)
            # flattened transition layer between conv and fully-conected layers
            flattened_layer = tf.contrib.layers.flatten(self.layers[-1])
            # construct fully-connected layers
            tmp_fc = tf.contrib.layers.fully_connected(flattened_layer,
                        fc_shapes[0], activation_fn=tf.tanh,
                        weights_initializer=tf.contrib.layers.xavier_initializer(),
                        biases_initializer=tf.constant_initializer(0.1),
                        scope='fc_1')
            self.layers.append(tmp_fc)

            for i in range(1, len(fc_shapes)):
                layer_label = "fc_" + str(i+1)
                tmp_fc = tf.contrib.layers.fully_connected(self.layers[-1],
                fc_shapes[i], activation_fn=tf.nn.relu,
                weights_initializer=tf.contrib.layers.xavier_initializer(),
                biases_initializer=tf.constant_initializer(0.1),
                scope=layer_label)
                self.layers.append(tmp_fc)

            self.outputs = self.layers[-1]

class RecNet(object):
    def __init__(self, input_shape, hidden_shape, n_layers, dropout):
        """Constructs a multi-layered recurrent neural network.

            Given an iterable of layer sizes and a dropout probability,
                assembles a tensorflow RNN with layers of those sizes and
                dropout applied to the outputs of those layers.

            Args:
                layer_shapes: An iterable implicitly specifying the number
                    of layers in the RNN, and explicitly specifying the shapes
                    of each layer.
                dropout_keep_prob: The percentage odds of each node's output
                    being replaced with zero.

            Returns:
                N/A

            Raises:
                AssertError: dropout probability is less than zero or greater than one
        """
        assert (dropout >= 0.0) and (dropout <= 1.0)
        self.input_shape = input_shape
        self.hidden_shape = hidden_shape
        self.output_shape = hidden_shape
        self.inputs = tf.placeholder(tf.float32, input_shape)
        rnn_cells = []
        with tf.variable_scope('rnn_model') as scope:
            lstm = tf.nn.rnn_cell.BasicLSTMCell(hidden_shape,
                        state_is_tuple=True)
            lstm = tf.nn.rnn_cell.DropoutWrapper(lstm, output_keep_prob=dropout)
            self.net = tf.nn.rnn_cell.MultiRNNCell([lstm] * n_layers,
                        state_is_tuple=True)
            # for shape in layer_shapes:
            #     tmp_cell = tf.nn.rnn_cell.BasicLSTMCell(shape,
            #         state_is_tuple=True)
            #     tmp_cell = tf.nn.rnn_cell.DropoutWrapper(tmp_cell,
            #         output_keep_prob=dropout_keep_prob)
            #     rnn_cells.append(tmp_cell)
            # self.net = tf.nn.rnn_cell.MultiRNNCell(rnn_cells,
            #     state_is_tuple=True)
        # fc_layer = tf.contrib.layers.fully_connected(self.rnn,
        #             fc_shape, activation_fn=tf.nn.relu,
        #             weights_initializer=tf.contrib.layers.xavier_initializer(),
        #             biases_initializer=tf.constant_initializer(0.1),
        #             scope="fc_1")
        # self.outputs = fc_layer


class C2SModel(object):
    def __init__(self, cnn, rnn, learning_rate, batch_size, rnn_seq_length,
                    fully_connected_shapes, alphabet, null_terminator,
                    embedding_size, max_seq_len):
        assert null_terminator in alphabet
        # Component networks
        self.cnn = cnn
        self.rnn = rnn
        # Model parameters
        self.lr = learning_rate
        self.batch_size = batch_size
        self.seq_len = max_seq_len
        self.alphabet = alphabet
        self.null_terminator = null_terminator
        self.img_embedding_size = embedding_size
        # Image embedding
        self.img_features = self.cnn.outputs
        self.img_embedding_weights = \
            tf.Variable(tf.truncated_normal([self.cnn.output_shape,
                self.rnn.hidden_shape], stddev=0.01))
        self.img_embedding_bias = tf.Variable(tf.constant(0.1,
                                    shape=[self.rnn.hidden_shape]))
        self.h0 = tf.matmul(self.img_features, self.img_embedding_weights) \
                    + self.img_embedding_bias
        self.c0 = tf.zeros_like(self.h0)
        # Character to one-hot
        vec = pandas.get_dummies(alphabet).to_dict()
        for k in vec.keys():
            vs = vec[k].values()
            vec[k] = tuple([v for v in vs])
        self.alph2vec = vec
        self.vec2alph = {value:key for key, value in self.alph2vec.items()}
        self.input_char = tf.placeholder(tf.float32, [self.batch_size,
                            self.seq_len, len(self.alphabet)])
        # Other
        self.step = 0

    def iupac_to_one_hots(self, iupac):
        one_hots = np.zeros([self.seq_len, len(self.alphabet)])
        seq_pos = 0
        for i in range(len(iupac)):
            one_hots[seq_pos] = self.alph2vec[iupac[i]]
            seq_pos += 1
        for i in range(len(iupac), self.seq_len):
            one_hots[seq_pos] = self.alph2vec[self.null_terminator]
            seq_pos += 1
        return one_hots

    def get_output(self):
        # self.input_char = tf.reshape(self.input_char, [self.batch_size, 1,
        #                     len(self.alphabet)])
        rnn_output, rnn_state = tf.nn.dynamic_rnn(self.rnn.net,
                                        self.input_char, dtype=tf.float32,
                                        initial_state=(self.c0, self.h0),
                                        sequence_length=[self.seq_len])
        rnn_output = tf.reshape(rnn_output, [self.seq_len,
                        self.rnn.output_shape])
        # rnn_output = tf.gather(rnn_output,
        #                 tf.range(self.get_data_length(self.seq_embedding)))
        fc = tf.contrib.layers.fully_connected(rnn_output, len(self.alphabet),
                activation_fn=tf.nn.relu,
                weights_initializer=tf.contrib.layers.xavier_initializer(),
                biases_initializer=tf.constant_initializer(0.1))
        prediction = tf.nn.softmax(fc)
        self.step += 1
        return prediction

    def train(self, train_samples, test_samples, iters, display_interval):
        pred = self.get_output()
        target = tf.placeholder(tf.float32, [1, self.seq_len,
                    len(self.alphabet)])
        cross_entropy = -tf.reduce_sum(target * tf.log(pred),
                            reduction_indices=[1])
        cross_entropy = tf.reduce_mean(cross_entropy)
        optimizer = tf.train.AdamOptimizer(learning_rate=self.lr,
                        epsilon=1e-2).minimize(cross_entropy)
        sess.run(tf.initialize_all_variables())

        initial_input = self.iupac_to_one_hots("")
        initial_input = np.reshape(initial_input,
                            [1, self.seq_len, len(self.alphabet)])
        for i in range(iters):
            batch = random.sample(train_samples, self.batch_size)
            xs = []
            ys = []
            for sample in batch:
                xs.append(sample[0])
                ys.append(sample[1])
            feed = {self.cnn.inputs: xs, target: ys,
                    self.input_char: initial_input}
            loss, _ = sess.run([cross_entropy, optimizer], feed_dict=feed)
            if self.step % display_interval == 0:
                print str(self.step) + ": " + str(loss)
            self.step += 1

    # def train(self, train_samples, test_samples, iters, display_interval):
    #     pred = self.get_output()
    #     target = tf.placeholder(tf.float32, [None, len(self.alphabet)])
    #     cross_entropy = -tf.reduce_sum(target * tf.log(pred),
    #                         reduction_indices=[1])
    #     cross_entropy = tf.reduce_mean(cross_entropy)
    #     optimizer = tf.train.AdamOptimizer(learning_rate=self.lr,
    #                     epsilon=1e-2).minimize(cross_entropy)
    #     sess.run(tf.initialize_all_variables())
    #     for i in range(iters):
    #         batch = random.sample(train_samples, self.batch_size)
    #         xs = []
    #         ys = []
    #         for sample in batch:
    #             xs.append(sample[0])
    #
    #             y = sample[1]
    #             ys.append(y)
    #         # print xs
    #         return

        # self.null_terminator = null_terminator
        # #assert self.null_terminator in self.alphabet
        # self.batch_size = batch_size
        # # Image embeddings
        # # self.img_features = tf.placeholder(tf.float32, [None,
        # #                         self.cnn.output_shape])
        # self.img_features = self.cnn.outputs
        # self.img_embedding_weights = \
        #     tf.Variable(tf.truncated_normal([self.cnn.output_shape,
        #         self.rnn.hidden_shape], stddev=0.01))
        # self.img_embedding_bias = tf.Variable(tf.constant(0.1,
        #                             shape=[self.rnn.hidden_shape]))
        # self.h0 = tf.matmul(self.img_features, self.img_embedding_weights) \
        #             + self.img_embedding_bias
        # self.c0 = tf.zeros_like(self.h0)
        # # Label embedding
        # self.embedding_size = embedding_size
        # self.max_seq_len = max_seq_len
        # self.seq_embedding_matrix = \
        #     tf.Variable(tf.random_uniform([len(self.alphabet)+1,
        #         self.rnn.input_shape[0]], -1.0, 1.0))
        # self.seq_input = tf.placeholder(tf.int32, [None])
        # self.seq_embedding = tf.concat(0,
        #     [tf.nn.embedding_lookup(self.seq_embedding_matrix,
        #         self.seq_input), tf.zeros([self.max_seq_len - \
        #         tf.shape(self.seq_input)[0], self.rnn.input_shape[0]])])
        # self.seq_embedding = tf.reshape(self.seq_embedding, [1, -1,
        #                         self.rnn.input_shape[0]])
        # # IO, params, and dictionary creation
        # self.x = np.zeros([self.batch_size, 30, 30, 1])
        # self.y = tf.placeholder(tf.float32, [None, len(alphabet)])
        # # self.output = tf.placeholder(tf.float32, [None,
        # #             len(alphabet)])
        # self.merged = tf.merge_all_summaries()
        # self.lr = learning_rate
        # self.fc_shapes = fully_connected_shapes
        # self.inputs = cnn.inputs
        # #vec = pandas.get_dummies(alphabet).to_dict()
        # self.numbered_alph = {}
        # for i in range(len(self.alphabet)):
        #     self.numbered_alph[self.alphabet[i]] = float(i)
        # self.numbered_alph["#"] = -1.0
        #
        # self.label_starts = [self.label_to_nums("#" + char) for char in\
        #                         self.alphabet]
        # self.label_ends = [char + "#" for char in self.alphabet]
        # self.label_starts = [np.eye(len(self.alphabet)+1)[l] for l in \
        #                         self.label_starts]
        # # for k in vec.keys():
        # #     vs = vec[k].values()
        # #     vec[k] = tuple([v for v in vs])
        # # self.alph2vec = vec
        # # self.vec2alph = {value:key for key, value in self.alph2vec.items()}
        # # self.rnn_state = self.rnn.net.zero_state(self.batch_size, tf.float32)
        # self.train_length = rnn_seq_length
        # self.step = 0

    # def label_to_nums(self, s):
    #     nums = np.zeros(len(s))
    #     for i in range(len(s)):
    #         nums[i] = self.numbered_alph[s[i]]
    #     return nums
    #
    # def get_data_length(self, data):
    #     used = tf.sign(tf.reduce_max(tf.abs(data), reduction_indices=2))
    #     length = tf.reduce_sum(used, reduction_indices=1)
    #     length = tf.cast(length, tf.int32)
    #     return length

    # def get_output(self):
    #     label = "rnn_" + str(self.step)
    #     self.img_features = self.cnn.outputs
    #     rnn_output, rnn_state = tf.nn.dynamic_rnn(self.rnn.net,
    #                                     self.seq_embedding, dtype=tf.float32,
    #                                     initial_state=(self.c0, self.h0),
    #                                     sequence_length=self.get_data_length\
    #                                         (self.seq_embedding))
    #     rnn_output = tf.reshape(rnn_output, [-1] + self.rnn.output_shape)
    #     rnn_output = tf.gather(rnn_output,
    #                     tf.range(self.get_data_length(self.seq_embedding)))
    #     fc = tf.contrib.layers.fully_connected(rnn_output, len(self.alphabet),
    #             activation_fn=tf.nn.relu,
    #             weights_initializer=tf.contrib.layers.xavier_initializer(),
    #             biases_initializer=tf.constant_initializer(0.1))
    #     prediction = tf.nn.softmax(fc)
    #     self.step += 1
    #     return prediction
    #
    # def train(self, train_samples, test_samples, iters, display_interval):
    #     pred = self.get_output()
    #     target = tf.placeholder(tf.float32, [None, len(self.alphabet)])
    #     cross_entropy = -tf.reduce_sum(target * tf.log(pred),
    #                         reduction_indices=[1])
    #     cross_entropy = tf.reduce_mean(cross_entropy)
    #     optimizer = tf.train.AdamOptimizer(learning_rate=self.lr,
    #                     epsilon=1e-2).minimize(cross_entropy)
    #     sess.run(tf.initialize_all_variables())
    #     for i in range(iters):
    #         batch = random.sample(train_samples, self.batch_size)
    #         xs = []
    #         ys = []
    #         for sample in batch:
    #             xs.append(sample[0])
    #
    #             y = sample[1]
    #             ys.append(y)
    #         # print xs
    #         return

if __name__ == "__main__":
    from tensorflow.examples.tutorials.mnist import input_data
    #mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
    batch_size = 1
    n_iters = 7000
    resolution = (30, 30)
    sample_input_shape = list(resolution) + [1]
    alphabet = [char for char in "abcdefghijklmnopqrstuvwxzy0123456789-#"]
    null_terminator = '#'
    summaries_dir = ""
    embedding_size = 820
    n_hidden = 820
    max_seq_len = 250

    cnn = ConvNet(resolution, [16, 8, 4], [200], [[6,6], [4,4],
            [2,2]], [[3,3], [3,3], [3,3]], batch_size)
    #rnn_input_shape = [50, batch_size, 3]
    rnn_input_shape = [len(alphabet)]
    rnn = RecNet(rnn_input_shape, n_hidden, 1, 0.6)
    c2s = C2SModel(cnn, rnn, 0.001, batch_size, max_seq_len, [200, 150, 100], alphabet,
            null_terminator, embedding_size, max_seq_len)

    samples = []
    for i in range(2000):
        y = []
        xs = np.random.rand(30,30,1) * len(alphabet)
        x_average = np.average(xs)
        x_median = np.median(xs)
        tmp_y = int(x_average * x_median / len(alphabet))
        one_hot = convert_to_one_hot(tmp_y, len(alphabet))
        for i in range(max_seq_len):
            y.append(one_hot)
            tmp_y += 1
        samples.append((xs, y))
    test_samples = []
    for i in range(200):
        y = []
        xs = np.random.rand(30,30,1) * len(alphabet)
        x_average = np.average(xs)
        x_median = np.median(xs)
        tmp_y = int(x_average * x_median / len(alphabet))
        one_hot = convert_to_one_hot(tmp_y, len(alphabet))
        for i in range(max_seq_len):
            y.append(one_hot)
            tmp_y += 1
        test_samples.append((xs, y))
    c2s.train(samples, test_samples, n_iters, display_interval=25)

    # with tf.variable_scope("c2s", reuse=None) as scope:
    #     c2s.get_output(np.ones([batch_size] + list(resolution)+ [1]), i)
    #     scope.reuse_variables()
        # for i in range(int(100)):
        #     c2s.get_output(np.ones([batch_size] + list(resolution)+ [1]), i)

    train_writer = tf.train.SummaryWriter(summaries_dir + "train", sess.graph)

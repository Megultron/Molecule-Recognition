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
    def __init__(self, input_shape, layer_shapes, dropout_keep_prob):
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
        assert (dropout_keep_prob >= 0.0) and (dropout_keep_prob <= 1.0)
        self.input_shape = input_shape
        self.output_shape = layer_shapes[-1]
        self.inputs = tf.placeholder(tf.float32, input_shape)
        rnn_cells = []
        with tf.variable_scope('rnn_model') as scope:
            for shape in layer_shapes:
                tmp_cell = tf.nn.rnn_cell.BasicLSTMCell(shape,
                    state_is_tuple=True)
                tmp_cell = tf.nn.rnn_cell.DropoutWrapper(tmp_cell,
                    output_keep_prob=dropout_keep_prob)
                rnn_cells.append(tmp_cell)
            self.net = tf.nn.rnn_cell.MultiRNNCell(rnn_cells,
                state_is_tuple=True)
        # fc_layer = tf.contrib.layers.fully_connected(self.rnn,
        #             fc_shape, activation_fn=tf.nn.relu,
        #             weights_initializer=tf.contrib.layers.xavier_initializer(),
        #             biases_initializer=tf.constant_initializer(0.1),
        #             scope="fc_1")
        # self.outputs = fc_layer

    def get_output(self, x):
        output, _ = tf.nn.dynamic_rnn(self.net, x, dtype=tf.float32,
                        scope="rnn_output")
        output = tf.transpose(output, [1, 0, 2])

    def get_dummy_output(self):
        x = tf.zeros(self.inputs.get_shape())
        self.get_output(x)


class C2SModel(object):
    def __init__(self, cnn, rnn, learning_rate, batch_size, rnn_seq_length,
                    fully_connected_shapes, alphabet):
        self.cnn = cnn
        self.rnn = rnn
        self.batch_size = batch_size
        self.y = tf.placeholder(tf.float32, [self.batch_size, len(alphabet)])
        self.merged = tf.merge_all_summaries()
        self.lr = learning_rate
        self.fc_shapes = fully_connected_shapes
        self.inputs = cnn.inputs
        self.alphabet = alphabet
        vec = pandas.get_dummies(alphabet).to_dict()
        for k in vec.keys():
            vs = vec[k].values()
            vec[k] = tuple([v for v in vs])
        self.alph2vec = vec
        self.vec2alph = {value:key for key, value in self.alph2vec.items()}
        self.rnn_state = self.rnn.net.zero_state(self.batch_size, tf.float32)
        self.train_length = rnn_seq_length
        self.step = 0

    def get_output(self):
        #with tf.variable_scope("model_outputs"):
        #     with tf.variable_scope("cnn"):
        #         cnn_output = sess.run(self.cnn.outputs,
        #                         feed_dict={self.cnn.inputs: x})
        #         cnn_output = cnn_output.tolist()
        #         #cnn_output = self.cnn.outputs
        cnn_output = self.cnn.outputs

        cnn_flat = tf.reshape(slim.flatten(cnn_output), \
                    [self.batch_size, self.train_length, self.rnn.input_shape[0]])
        with tf.variable_scope("rnn"):
            label = "rnn_" + str(self.step)
            # rnn_output, self.rnn_state = self.rnn.net(self.cnn.outputs,
            #                                 self.rnn_state, scope=label)
            rnn_output, self.rnn_state = \
                tf.nn.dynamic_rnn(\
                    self.rnn.net, cnn_flat, dtype=tf.float32,
                    initial_state=self.rnn_state)
            rnn_output = tf.reshape(rnn_output, [-1, self.rnn.output_shape])
            # rnn_output = tf.slice(rnn_output, [1, 0, 0],
            #                 [0, -1, -1])
            #rnn_output = tf.split(0, self.batch_size, rnn_output)[0]

        with tf.variable_scope("softmax"):
            fc = tf.contrib.layers.fully_connected(rnn_output, \
                    len(self.alphabet), activation_fn=tf.nn.relu,
                    weights_initializer= \
                        tf.contrib.layers.xavier_initializer(),
                    biases_initializer=tf.constant_initializer(0.1))
            # sm = tf.nn.softmax(fc, name="softmax_"+str(self.step))

            #     tf.scalar_summary("output", rnn_output)
            #     summary = sess.run([self.merged, rnn_output])
            #     self.train_writer.add_summary(summary, self.step)
        self.rnn_state = self.rnn.net.zero_state(self.batch_size, tf.float32)
        self.step += 1
        return fc

    def train(self, train_samples, test_samples, iters, display_interval):
        pred = self.get_output()
        #ce = tf.nn.sigmoid_cross_entropy_with_logits(pred, self.y)
        ce = tf.nn.softmax_cross_entropy_with_logits(pred, self.y)
        loss = tf.reduce_mean(ce)
        optimizer = \
            tf.train.RMSPropOptimizer(learning_rate=self.lr).minimize(loss)
        sess.run(tf.initialize_all_variables())
        print "TRAINING"
        for i in range(iters):
            batch = random.sample(train_samples, self.batch_size)
            xs = []
            ys = []
            for sample in batch:
                xs.append(sample[0])
                y = sample[1]
                y = self.vec2alph.keys()[y]
                ys.append(y)
            # pred = self.get_output(xs, i)
            # ce = tf.nn.sigmoid_cross_entropy_with_logits(pred + 1e-6, ys)
            # loss = tf.reduce_mean(ce)
            # optimizer = tf.train.RMSPropOptimizer(learning_rate=self.lr)
            # train_step = optimizer.minimize(loss)

            sess.run(optimizer, feed_dict={self.cnn.inputs: xs, self.y: ys})
            if i % display_interval == 0:
                print str(i) + ": " + \
                    str(sess.run(loss, feed_dict={self.cnn.inputs: xs,
                                                self.y: ys}))

        print "\nTRAINING COMPLETE\n--------------------------------"
        print "TESTING"
        total_loss = 0.0
        for sample in test_samples:
            x = [sample[0]]
            y = sample[1]
            y = self.vec2alph.keys()[y]
            result, step_loss = sess.run([pred, loss], feed_dict= \
                                {self.cnn.inputs: x, self.y: ys})
            # print "TARGET: " + str(y)
            # print "PREDICTION: " + str(result)
            # print "LOSS: " + str(step_loss)
            total_loss += step_loss
        print "AVG TEST LOSS: " + str(total_loss / len(test_samples))
        print "\nTESTING COMPLETE\n--------------------------------"

if __name__ == "__main__":
    from tensorflow.examples.tutorials.mnist import input_data
    #mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
    batch_size = 1
    resolution = (64, 64)
    sample_input_shape = list(resolution) + [1]
    alphabet = [char for char in "0123456789abcdef#!,"]
    summaries_dir = ""

    cnn = ConvNet(resolution, [16, 8, 4], [100, 80, 50], [[6,6], [4,4],
            [2,2]], [[3,3], [3,3], [3,3]], batch_size)
    #rnn_input_shape = [50, batch_size, 3]
    rnn_input_shape = [50]
    rnn = RecNet(rnn_input_shape, [300, 200, 100], 0.5)
    c2s = C2SModel(cnn, rnn, 0.001, batch_size, 1, [150, 100, 75], alphabet)

    # sess.run(tf.initialize_all_variables())
    rnn_input_size = 50
    samples = []
    for i in range(8000):
        xs = np.random.rand(64,64,1)*len(alphabet)
        y = int(np.average(xs))
        samples.append((xs, y))
    test_samples = []
    for i in range(4000):
        xs = np.random.rand(64,64,1)*len(alphabet)
        y = int(np.average(xs))
        test_samples.append((xs, y))
    c2s.train(samples, test_samples, 500, display_interval=10)

    # with tf.variable_scope("c2s", reuse=None) as scope:
    #     c2s.get_output(np.ones([batch_size] + list(resolution)+ [1]), i)
    #     scope.reuse_variables()
        # for i in range(int(100)):
        #     c2s.get_output(np.ones([batch_size] + list(resolution)+ [1]), i)

    train_writer = tf.train.SummaryWriter(summaries_dir + "train", sess.graph)

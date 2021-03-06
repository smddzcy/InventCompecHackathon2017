import os
import tensorflow as tf
import numpy as np
import datetime as dt
import itertools
from sklearn.model_selection import train_test_split
from numpy import genfromtxt

# Display the status on each nth step
display_step = 10
# Number of training steps
steps = 1000
# Learning rate to use on the optimizer
learn_rate = 0.001
# Path to save the trained model
path = path = os.path.dirname(os.path.realpath(__file__))
model_path = path + "/model_files/multivariate-model.ckpt"

RANDOM_SEED = 42
tf.set_random_seed(RANDOM_SEED)

def one_hot(num, num_classes):
    """ Creates a one-hot vector with given num and num_classes """
    return np.eye(num_classes)[num].astype(int)

def flatten(arr):
    return np.array(list(itertools.chain.from_iterable(arr)))

def get_data():
    """ Read the data set and split it into training and test sets """
    data   = genfromtxt('data_big.csv', delimiter=',')
    data_in = data[:, [0, 1, 2, 3, 4]]

    def map_fn(row):
        """ Splits the date column into 4 one-hot boolean vectors """
        result = np.array(row)
        date = dt.datetime.strptime(str(int(row[0])), "%Y%m%d").timetuple()
        res = flatten(np.array([one_hot(date.tm_wday, 7), one_hot(date.tm_mday - 1, 31),
                one_hot(date.tm_yday - 1, 366), one_hot(date.tm_mon - 1, 12), row[1:]]))
        return res

    data_in = np.array(map(map_fn, data_in))
    data_out = data[:, [5]]

    return train_test_split(data_in, data_out, test_size=0.1, random_state=RANDOM_SEED)

train_X, test_X, train_Y, test_Y = get_data()

# Normalize each column in the matrix
normalization_values = np.zeros((train_X.shape[1], 2))

def normalize_matrix(matrix):
    for i in range(matrix.shape[1]):
        mean = np.mean(matrix[:, [i]], axis=0)
        matrix[:, [i]] -= mean
        std = np.std(matrix[:, [i]], axis=0)
        if std != 0:
            matrix[:, [i]] /= np.std(matrix[:, [i]], axis=0)
        normalization_values[i] = [mean, std]
    return matrix

train_X = normalize_matrix(train_X)

x = tf.placeholder(tf.float32, [None, train_X.shape[1]], name="x")
y_ = tf.placeholder(tf.float32, name="y_")

W = tf.Variable(tf.zeros([train_X.shape[1],1]), name="W")
b = tf.Variable(tf.zeros([1]), name="b")
y = tf.add(tf.matmul(x,W), b)

# Cost function sum((y_-y)**2)
cost = tf.reduce_mean(tf.square(y_-y))
optimizer = tf.train.GradientDescentOptimizer(learn_rate).minimize(cost)

# 'Saver' op to save and restore all the variables
saver = tf.train.Saver()

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(steps):
      sess.run(optimizer, feed_dict={ x: train_X, y_: train_Y })

      if i % display_step == 0:
          print("After %d iteration:" % i)
          print("W: %s" % sess.run(W))
          print("b: %f" % sess.run(b))
          print("cost: %f" % sess.run(cost, feed_dict={ x: test_X, y_: test_Y }))

    print("Training is finished.")

    # Print the normalization values for future use
    print("Normalization values:")
    print(normalization_values)

    # Save model weights to disk
    save_path = saver.save(sess, model_path)
    print("Model saved in file: %s" % save_path)

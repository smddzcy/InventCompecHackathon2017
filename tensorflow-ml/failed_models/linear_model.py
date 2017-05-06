import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from numpy import genfromtxt

# CUSTOMIZABLE: Collect/Prepare data
display_step = 100
steps = 10000
learn_rate = 0.001

RANDOM_SEED = 42
tf.set_random_seed(RANDOM_SEED)

def get_data():
    """ Read the data set and split it into training and test sets """
    data   = genfromtxt('data.csv', delimiter=',')
    data_in = data[:, [0, 1, 2, 3, 4, 5]]
    data_out = data[:, [6]]

    return train_test_split(data_in, data_out, test_size=0.1, random_state=RANDOM_SEED)

train_X, test_X, train_Y, test_Y = get_data()

# Normalize each column in the matrix
for i in range(train_X.shape[1]):
    train_X[:, [i]] -= np.mean(train_X[:, [i]], axis=0)
    std = np.std(train_X[:, [i]], axis=0)
    if std != 0:
        train_X[:, [i]] /= np.std(train_X[:, [i]], axis=0)

x = tf.placeholder(tf.float32, [None, train_X.shape[1]], name="x")
y_ = tf.placeholder(tf.float32, name="y_")

W = tf.Variable(tf.zeros([train_X.shape[1],1]), name="W")
b = tf.Variable(tf.zeros([1]), name="b")
y = tf.add(tf.matmul(x,W), b)

# Cost function sum((y_-y)**2)
cost = tf.reduce_mean(tf.square(y_-y))
optimizer = tf.train.AdamOptimizer(learn_rate).minimize(cost)

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

# Implementation of a simple MLP network with one hidden layer.
import tensorflow as tf
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from numpy import genfromtxt

RANDOM_SEED = 42
tf.set_random_seed(RANDOM_SEED)

def init_weights(shape):
    """ Weight initialization"""
    weights = tf.zeros(shape)
    return tf.Variable(weights)

def forwardprop(X, w_1, w_2):
    """
    Forward-propagation. Note that yhat is not softmax since TensorFlow's
    softmax_cross_entropy_with_logits() does that internally.
    """
    h    = tf.nn.sigmoid(tf.matmul(X, w_1))  # The \sigma function
    yhat = tf.matmul(h, w_2)  # The \varphi function
    return yhat

def convertToOneHot(vector, num_classes=None):
    """
    Converts an input 1-D vector of integers into an output
    2-D array of one-hot vectors, where an i'th input value
    of j will set a '1' in the i'th row, j'th column of the
    output array.

    Example:
        v = np.array((1, 0, 4))
        one_hot_v = convertToOneHot(v)
        print one_hot_v

        [[0 1 0 0 0]
         [1 0 0 0 0]
         [0 0 0 0 1]]
    """

    assert isinstance(vector, np.ndarray)
    assert len(vector) > 0

    if num_classes is None:
        num_classes = np.max(vector)+1
    else:
        assert num_classes > 0
        assert num_classes >= np.max(vector)

    result = np.zeros(shape=(len(vector), num_classes))
    result[np.arange(len(vector)), vector] = 1
    return result.astype(int)

def get_data():
    """ Read the data set and split it into training and test sets"""
    data   = genfromtxt('data2.csv', delimiter=',')
    data_in  = data[:, [0, 1, 2, 3, 4, 5]]
    data_out = data[:, [6]].astype(int).flatten()
    # Clear negative values from sales quantity, which breaks the neural network
    data_out[data_out < 0] = 0

    # Prepend the column of 1s for bias
    N, M  = data_in.shape
    all_X = np.ones((N, M + 1))
    all_X[:, 1:] = data_in

    # Convert into one-hot vectors
    all_Y = convertToOneHot(data_out, 190)
    return train_test_split(all_X, all_Y, test_size=0.25, random_state=RANDOM_SEED)

def main():
    # Get training and test data
    train_X, test_X, train_y, test_y = get_data()

    # NOTE: In order to make the code simple, we rewrite x * W_1 + b_1 = x' * W_1'
    # where x' = [x | 1] and W_1' is the matrix W_1 appended with a new row with elements b_1's.
    # Similarly, for h * W_2 + b_2

    # Layer's sizes
    x_size = train_X.shape[1]   # Number of input nodes: 4 features and 1 bias
    h_size = 256                # Number of hidden nodes
    y_size = train_y.shape[1]   # Number of outcomes (3 iris flowers)

    # Symbols
    X = tf.placeholder("float", shape=[None, x_size])
    y = tf.placeholder("float", shape=[None, y_size])

    # Weight initializations
    w_1 = init_weights((x_size, h_size))
    w_2 = init_weights((h_size, y_size))

    # Forward propagation
    yhat    = forwardprop(X, w_1, w_2)
    predict = tf.argmax(yhat, axis=1)

    # Backward propagation
    cost    = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=yhat))
    updates = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

    # Run SGD
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    for epoch in range(100):
        # Train with each example
        for i in range(len(train_X)):
            sess.run(updates, feed_dict={X: train_X, y: train_y})

        train_accuracy = np.mean(np.argmax(train_y, axis=1) ==
                                 sess.run(predict, feed_dict={X: train_X, y: train_y}))

        print np.argmax(test_y, axis=1)
        print sess.run(predict, feed_dict={X: test_X, y: test_y})
        test_accuracy  = np.mean(np.argmax(test_y, axis=1) ==
                                 sess.run(predict, feed_dict={X: test_X, y: test_y}))

        print("Epoch = %d, train accuracy = %.2f%%, test accuracy = %.2f%%"
              % (epoch + 1, 100. * train_accuracy, 100. * test_accuracy))

    sess.close()

if __name__ == '__main__':
    main()

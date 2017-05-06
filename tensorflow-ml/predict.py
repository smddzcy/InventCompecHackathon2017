#!/usr/bin/python

import sys, os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
import json

# Normalize each column in the matrix
def normalize_matrix(matrix):
    for i in range(matrix.shape[1]):
        matrix[:, [i]] -= np.mean(matrix[:, [i]], axis=0)
        std = np.std(matrix[:, [i]], axis=0)
        if std != 0:
            matrix[:, [i]] /= np.std(matrix[:, [i]], axis=0)
    return matrix

def main(argv):
    # Initialize the variables before restoring
    x = tf.placeholder(tf.float32, [None, 6], name="x")
    y_ = tf.placeholder(tf.float32, name="y_")
    W = tf.Variable(tf.zeros([6,1]), name="W")
    b = tf.Variable(tf.zeros([1]), name="b")
    y = tf.add(tf.matmul(x,W), b)

    with tf.Session() as sess:
        saver = tf.train.Saver()
        # Restore the trained model
        path = os.path.dirname(os.path.realpath(__file__))
        saver.restore(sess, path + "/model_files/multivariate-model.ckpt")
        predict_in = np.asarray(json.loads(argv[0]))
        predict_in = normalize_matrix(predict_in)
        result = sess.run(y, feed_dict={ x: predict_in })
        print(json.dumps(result.tolist()))

if __name__ == "__main__":
   main(sys.argv[1:])

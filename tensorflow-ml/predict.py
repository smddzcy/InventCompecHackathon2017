#!/usr/bin/python

import sys, os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
import json

normalization_values = np.asarray([[15.75530922,8.9341489],
                                   [7.18106597,3.62328201],
                                   [1582.7119876,893.55621648],
                                   [11.14583395,7.08089889],
                                   [244.54959832,94.4803919],
                                   [69.22979744,70.08119565]])

# Normalize each column in the matrix
def normalize_matrix(matrix):
    for i in range(matrix.shape[1]):
        matrix[:, [i]] -= normalization_values[i, 0]
        std = normalization_values[i, 1]
        if std != 0:
            matrix[:, [i]] /= std
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
        predict_in = np.asarray(json.loads(argv[0])).astype(float)
        print(predict_in)
        predict_in = normalize_matrix(predict_in)
        print(normalize_matrix(np.asarray([[1.,1.,101.,3.,10.,170.5]])))
        print(predict_in)
        result = sess.run(y, feed_dict={ x: predict_in })
        print(json.dumps(result.tolist()))

if __name__ == "__main__":
   main(sys.argv[1:])

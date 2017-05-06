import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from numpy import genfromtxt

RANDOM_SEED = 42
tf.set_random_seed(RANDOM_SEED)

def get_data():
    """ Read the data set and split it into training and test sets """
    data   = genfromtxt('data.csv', delimiter=',')
    data_in = data[:, [0, 1, 2, 3, 4, 5]]
    data_out = data[:, [6]].astype(int).flatten()
    # Clear negative values
    data_out[data_out < 0] = 0

    return train_test_split(data_in, data_out, test_size=0.25, random_state=RANDOM_SEED)

train_X, test_X, train_Y, test_Y = get_data()
X_size = train_X.shape[1]

features = [tf.contrib.layers.real_valued_column("day", dimension=1, dtype=tf.int32),
            tf.contrib.layers.real_valued_column("month", dimension=1, dtype=tf.int32),
            tf.contrib.layers.real_valued_column("day_month", dimension=1, dtype=tf.int32),
            tf.contrib.layers.real_valued_column("store_id", dimension=1, dtype=tf.int32),
            tf.contrib.layers.real_valued_column("product_id", dimension=1, dtype=tf.int32),
            tf.contrib.layers.real_valued_column("price", dimension=1, dtype=tf.float32)]

estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

input_fn = tf.contrib.learn.io.numpy_input_fn({
    "day": train_X[:, [0]],
    "month": train_X[:, [1]],
    "day_month": train_X[:, [2]],
    "store_id": train_X[:, [3]],
    "product_id": train_X[:, [4]],
    "price": train_X[:, [5]]
}, train_Y, batch_size=50, num_epochs=10000)


estimator.fit(input_fn=input_fn, steps=1000)

print estimator.evaluate(input_fn=tf.contrib.learn.io.numpy_input_fn({
    "day": test_X[:, [0]],
    "month": test_X[:, [1]],
    "day_month": test_X[:, [2]],
    "store_id": test_X[:, [3]],
    "product_id": test_X[:, [4]],
    "price": test_X[:, [5]]
}, test_Y))

def new_samples():
  return {
    "day": np.array([4, 4, 4, 4]),
    "month": np.array([7, 7, 7, 7]),
    "day_month": np.array([47, 47, 47, 47]),
    "store_id": np.array([9, 11, 5, 14]),
    "product_id": np.array([31, 31, 31, 31]),
    "price": np.array([127.0, 130.4, 125.6, 130.5])
  }


for i in estimator.predict(input_fn=new_samples):
    print i

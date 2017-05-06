# Machine Learning - TensorFlow

After trying many models with many different parameters - convolutional neural networks,
linear and logistic models - we've found a model that fits the best, which is
a basic multivariate linear regression model.

There are 6 1-dimensional features and 1 bias vector in the model. Predicted value
is the sales quantity. The features are:

|Feature|Explanation|
|---|---------------|
|`day`|Day of the month.|
|`month`|Month of the year, left padded with 0 to 2 digits.|
|`day_month`|Day & month together, to account special days in the model.|
|`store_id`|Code of the store.|
|`product_id`|Code of the product.|
|`price`|Price of the product, which can change and which we'll use to suggest better prices to the customer for specific products.|

## Some Important Files
- `data.csv` file contains the inputs and real world outputs. Features are on the
first 5 columns and the outputs are on the 6th column.
- `model_files` folder contains the trained TensorFlow model files - graphs, variables
and checkpoints.
- `train_model.py` trains the model, which should be executed only once.
- `predict.py` does the predictions using the trained model. It gets an `argv`
input which is an array of arrays containing feature values, and prints an array
containing the predicted sales quantities.

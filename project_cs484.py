import pandas as pd
import numpy as np
from scipy.optimize import least_squares
from sklearn.model_selection import train_test_split

# load data from CSV file into a pandas DataFrame
data = pd.read_csv('data.csv')

# extract labels and features from the DataFrame
labels = data.iloc[:, 0].astype(float)
features = data.iloc[:, 1:7].values

# standardize the features and labels
features = (features - features.mean(axis=0)) / features.std(axis=0)
labels = (labels - labels.mean()) / labels.std()

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# define a non-linear function to fit the data
def func(params, x):
    a, b, c, d, e, f = params
    return a * np.exp(-b * x[:,0]) + c * x[:,1]**2 + d * np.sin(e * x[:,2]) + f * x[:,3] ** 3 + (a+b+c) * np.exp(-d * x[:,4]) + e * x[:,5]

# define the residual function to be minimized
def residual(params, x, y):
    return func(params, x) - y

# perform curve fitting using L2 norm on training data
params0 = np.array([1, 1, 1, 1, 1, 1])
res = least_squares(residual, params0, args=(X_train, y_train))

# print the optimal parameters of the fitted function
a_fit, b_fit, c_fit, d_fit, e_fit, f_fit = res.x
print(f"a: {a_fit:.3f}, b: {b_fit:.3f}, c: {c_fit:.3f}, d: {d_fit:.3f}, e: {e_fit:.3f}, f: {f_fit:.3f}")

# use the fitted function to predict the labels of the testing set
y_pred = func(res.x, X_test)

# calculate the mean squared error of the predictions on the testing set
mse = ((y_pred - y_test) ** 2).mean()
print(f"Mean squared error: {mse:.3f}")
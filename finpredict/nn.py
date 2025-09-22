from sklearn.neural_network import *
import string

def get_nn_model(x,y):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x,y)
    return clf


def get_nn_regression_model(x,y):
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x,y)
    return clf

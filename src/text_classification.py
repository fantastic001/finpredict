import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import *
import string
import os 


def get_text_model(x,y):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x,y)
    return clf

def get_text_regression_model(x,y):
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x,y)
    return clf


def tokenize(text):
    text = list(c for c in text if c in (string.ascii_letters + " "))
    curr = "" 
    res = [] 
    for c in text:
        if c == " " and curr != "":
            res.append(curr)
            curr = ""
        if c != " ":
            curr += c
    if curr != "":
        res.append(curr)
    return list(w.lower() for w in res)

def extract(text, cat):
    return (tokenize(text), cat)

def get_vocabulary(x):
    """
    x is list of tuples (text, category)
    """
    x = list([extract(text, cat) for text,cat in x])
    words = set(w for w in sum([text for text,cat in x], []))
    words = list(words)
    return {w: i for w,i in zip(words, range(len(words)))}

def get_bow(x, words):
    """
    words: vocabulary from get_vocabulary(x)
    """
    result = []
    n = len(words.items())
    for text, cat in x:
        xx = np.zeros(n)
        for w in text:
            try:
                xx[words[w]] += 1
            except KeyError:
                pass
        result.append(xx)
    return result


def fit_nb(x):
    words = get_vocabulary(x)
    x = list(extract(a,b) for a,b in x)
    X = get_bow(x, words)
    y = list(set(cat for text,cat in x))
    clf = MultinomialNB()
    clf.fit(X, y)
    return (clf, words)


def predict_nb(clf, words, text):
    return clf.predict(get_bow([(tokenize(text), 0)], words))


def get_model_from_data(training_dir):
    x = []
    for c in os.listdir():
        for fpath in os.listdir("%s/%s/" % (training_dir, c)):
            f = open("%s/%s/%s" % (training_dir, c, fpath))
            text = f.read()
            f.close()
            x.append((text, int(c)))
    clf, words = fit_nb(x)
    return clf, words

def classify_content(fpath, clf, words):
    f = open(fpath)
    text = f.read()
    y = predict_nb(clf, words, text)
    return y[0]
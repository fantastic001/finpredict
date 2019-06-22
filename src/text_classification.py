import numpy as np
from sklearn.naive_bayes import MultinomialNB

import string

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


# Example of usage
# >>> text = "this is some nice text. This text is great"
# >>> x = [(text, 0)]
# >>> clf, words = fit_nb(x)
# >>> predict_nb(clf, words, "haha")
# array([0])

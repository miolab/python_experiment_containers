import numpy as np

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

import matplotlib.pyplot as plt


def init_test():
    return "sklearn_exam_test"


def fn_load_breast_cancer():
    global x_train, x_test, y_train, y_test

    brest_cancer = load_breast_cancer()
    print(type(brest_cancer))

    # 説明変数
    x = brest_cancer['data']
    # 目的変数
    y = brest_cancer['target']
    print(type(x), x.shape)
    print(type(y), y.shape)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0)
    print(x[:5])
    print(y[:5])

    print("benign(y=0) :", len(y[y == 0]))
    print("malignant (y=1):", len(y[y == 1]))


fn_load_breast_cancer()


def fn_decision_tree():
    fn_load_breast_cancer()

    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(x_train, y_train)

    t_test = clf.predict(x_test)
    clf.score(x_test, y_test)
    clf.score(x_train, y_train)


fn_decision_tree()

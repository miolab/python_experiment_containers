import sklearn
from sklearn.datasets import load_breast_cancer

brest_cancer = load_breast_cancer()
print(type(brest_cancer))

# 説明変数
x = brest_cancer['data']

# 目的変数
y = brest_cancer['target']

print(type(x), x.shape)
print(type(y), y.shape)

print(x[:5])
print(y[:5])

print("benign(y=0) :", len(y[y == 0]))
print("malignant (y=1):", len(y[y == 1]))

# -*- coding: utf-8 -*-
"""1465_logistic_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZUUfkMFfT-dCHrl4TH6rvsCbPRtP8wj3

# Logistic Regression
"""

from google.colab import drive
drive.mount('/content/drive')

"""## Importing the libraries"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Mllab/Datasets/50_Startups.csv')
X = dataset.iloc[:, :-3].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

"""# Label Encoding

## 50 Startups (Encoded State Coloum)
"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

"""### Total Profit Lable"""

a = 0
for value in y: 
  a = a+value
print(a)

avg = a/len(y)
label = []

for i in y:
  label.append(0) if i > avg else label.append(1)
y = np.array(label)
y

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

print(X_train)

print(y_train)

print(X_test)

print(y_test)

"""## Feature Scaling (Write appropriate code for feature scaling)"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# print(X_train)

# print(X_test)

"""## Training the Logistic Regression model on the Training set"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)
#classifier.fit(X_train, y_train)

"""## Predicting a new result"""

print(classifier.predict(X_test))

"""## Predicting the Test set results"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""## Visualising the Training set results"""

min1, max1 = X_train[:, 0].min()-1, X_train[:, 0].max()+1
min2, max2 = X_train[:, 1].min()-1, X_train[:, 1].max()+1
x1grid = np.arange(min1, max1, 0.1)
x2grid = np.arange(min2, max2, 0.1)
xx, yy = np.meshgrid(x1grid, x2grid)
r1, r2 = xx.flatten(), yy.flatten()
r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
grid = np.hstack((r1,r2))
yhat = classifier.predict_proba(grid)
yhat = yhat[:, 0]
zz = yhat.reshape(xx.shape)
c = plt.contourf(xx, yy, zz, cmap='RdBu')
plt.colorbar(c)
for class_value in range(2):
    row_ix = np.where(y_train == class_value)
    plt.scatter(X_train[row_ix, 0], X_train[row_ix, 1], cmap='Paired')

"""## Visualising the Test set results"""

min1, max1 = X_test[:, 0].min()-1, X_test[:, 0].max()+1
min2, max2 = X_test[:, 1].min()-1, X_test[:, 1].max()+1
x1grid = np.arange(min1, max1, 0.1)
x2grid = np.arange(min2, max2, 0.1)
xx, yy = np.meshgrid(x1grid, x2grid)
r1, r2 = xx.flatten(), yy.flatten()
r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
grid = np.hstack((r1,r2))
yhat = classifier.predict_proba(grid)
yhat = yhat[:, 0]
zz = yhat.reshape(xx.shape)
c = plt.contourf(xx, yy, zz, cmap='RdBu')
plt.colorbar(c)
for class_value in range(2):
    row_ix = np.where(y_test == class_value)
    plt.scatter(X_test[row_ix, 0], X_test[row_ix, 1], cmap='Paired')
# -*- coding: utf-8 -*-
"""Untitled220.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nAr8u6LIh3wjGrfTv0BSQidb3hHWfYuj
"""

import pickle
import pandas as pd
data = pd.read_csv('credit_data.csv')
data.drop(['clientid'], axis=1, inplace=True)
x = data.iloc[:,0:4]
y = data['default']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
#Fitting model with trainig data
model1 = model.fit(x, y)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6,7]]))


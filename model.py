# Importing the libraries
#from datetime import datetime
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('day2.csv')

# Converting words to integer values
df['season'] = df['season'].astype('category')
df['yr'] = df['yr'].astype('int')
df['mnth'] = df['mnth'].astype('category')
df['holiday'] = df['holiday'].astype('int')
df['workingday'] = df['workingday'].astype('int')
df['weekday'] = df['weekday'].astype('category')
df['weathersit'] = df['weathersit'].astype('category')
df = df.drop(['instant', 'casual', 'registered'], axis=1)
df = df.drop(['atemp'], axis=1)

X = df.drop(['cnt'], axis=1)
y = df['cnt']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

# Fitting model with trainig data
regressor.fit(X_train, y_train)

# Saving model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
#print(model.predict([["01-01-11", 1, 0, 1, 0, 6, 0, 2, 0.344167, 0.363625, 0.805833, 0.160446, 331, 654]]))
print(model.predict(X_test))

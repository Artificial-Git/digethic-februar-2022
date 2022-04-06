from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import PolynomialFeatures
# import matplotlib.pyplot as plt
# import random
# from time import time
import numpy as np
import pandas as pd
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
import pickle

# %matplotlib inline


def rmse(y_pred, y):
    return np.sqrt(np.mean((y_pred-y)**2))


# name=True bedeutet, dass Header als solche gespeichert werden.
# auto_array[i] gibt alle Attribute der iten Instanz, auto_array["attribut"] gibt "attribut" aller
# # Instanzen raus.
# auto_array = np.genfromtxt('../data/auto-mpg.csv', dtype=float, delimiter=";", names=True)
# data = pd.read_csv('../data/auto-mpg.csv', sep=";")
data = pd.read_csv('data/auto-mpg.csv', sep=";")

print(data)

# Daten vermischen. "n =" gibt an, wieviele Reihen abgefragt werden sollen, oder "frac = " gibt an,
# # welcher Anteil an allen Reihen abgefragt werden soll.
data = data.sample(frac=1)

# 'class'-Spalte
y_variable = data['mpg']

# Alle Spalten, die nicht in der 'class'-Spalte sind -> alle Spalten, die die Attribute enthalten.
# # Man kann loc[:,'attributname'], rausgeben lassen, oder loc[index,:]
x_variables = data.loc[:, data.columns != 'mpg']

x_train, x_test, y_train, y_test = train_test_split(
    x_variables, y_variable, test_size=0.2)

regressor = LinearRegression()

regressor = regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

# wb: öffnen für writing und im Binärmodus
# file_to_write = open("../data/models/baummethoden_lr.pickle", "wb")
file_to_write = open("data/models/baummethoden_lr.pickle", "wb")
pickle.dump(regressor, file_to_write)

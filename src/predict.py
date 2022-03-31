import pandas as pd
import pickle

# Trainiertes Modell laden. 'rb': read Binärdatei
file_to_open = open("../data/models/baummethoden_lr.pickle", 'rb')
trained_model = pickle.load(file_to_open)
file_to_open.close()

# Lade Daten, für die wir Vorhersagen wollen
prediction_data = pd.read_csv('../data/prediction-data.csv', sep=";")

#print(trained_model.predict(prediction_data.loc[:, prediction_data.columns != 'mpg']))

auto = [None]*5

auto[0] = int(input("Geben Sie die Anzahl der Zylinder ein: "))
auto[1] = float(input("Geben Sie die Leistung in PS an: "))
auto[2] = float(input("Geben Sie die Masse in kg an: "))
auto[3] = float(input("Geben Sie die Beschleunigung in 100 km/h/s an: "))
auto[4] = int(input("Geben Sie das Baujahr an: "))

print(trained_model.predict([auto]))

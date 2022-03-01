import pandas as pd
import pickle

# Trainiertes Modell laden. 'rb': read Binärdatei
file_to_open = open("../data/models/baummethoden_lr.pickle", 'rb')
trained_model = pickle.load(file_to_open)
file_to_open.close()

# Lade Daten, für die wir Vorhersagen wollen
prediction_data = pd.read_csv('../data/auto-mpg.csv', sep=";")

print(trained_model.predict(
    prediction_data.loc[:, prediction_data.columns != 'mpg']))

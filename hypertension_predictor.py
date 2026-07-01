import pickle
import numpy as np

model = pickle.load(
    open("models/hypertension_model.pkl", "rb")
)

def predict_hypertension(data):

    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    return prediction, probability
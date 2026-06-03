import joblib
import numpy as np


model = joblib.load("model.pkl")


def predict_risk(glucose, haemoglobin, cholesterol):

    features = np.array([
        [glucose, haemoglobin, cholesterol]
    ])

    prediction = model.predict(features)

    return prediction[0]
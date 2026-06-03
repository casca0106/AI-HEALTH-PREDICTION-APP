import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import joblib


data = pd.read_csv("dataset/health_data.csv")


X = data[["glucose", "haemoglobin", "cholesterol"]]

y = data["risk"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LogisticRegression()


model.fit(X_train, y_train)


joblib.dump(model, "model.pkl")


print("Model trained and saved successfully!")
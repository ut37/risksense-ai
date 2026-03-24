import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

X = np.random.rand(100, 30)
y = np.random.randint(0, 2, 100)

model = RandomForestClassifier()
model.fit(X, y)

with open("risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model recreated successfully")
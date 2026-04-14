import joblib

model = joblib.load("fraud_model.pkl")

def predict_risk(amount, hour, failed_attempts, is_new_device, avg_amount):
    features = [[amount, hour, failed_attempts, is_new_device, avg_amount]]

    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]  # 0–1 range

    return pred, prob
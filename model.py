import joblib

model = joblib.load("fraud_model.pkl")

def predict_risk(amount, hour, failed_attempts, is_new_device, avg_amount):
    features = [[amount, hour, failed_attempts, is_new_device, avg_amount]]

    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    risk = round(prob * 100)

    if pred == 0:
        risk = max(risk, 5)
    else:
        risk = max(risk, 75)

    return pred, risk
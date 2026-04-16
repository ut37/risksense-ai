import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), "fraud_model.pkl")
model = joblib.load(model_path)

def predict_risk(amount, hour, failed_attempts, is_new_device, avg_amount):
    features = [[amount, hour, failed_attempts, is_new_device, avg_amount]]

    
    prob = model.predict_proba(features)[0][1]  
  
    if prob > 0.5:
        pred = 1   
    else:
        pred = 0   

    return pred, prob
   
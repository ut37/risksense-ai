<<<<<<< HEAD
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '1234':
            return redirect('/welcome')   # 🔥 animation page

        return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# WELCOME ANIMATION PAGE
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')


if __name__ == '__main__':
=======
from flask import Flask, render_template, request
import joblib
import random

app = Flask(__name__)

# Load trained model
model = joblib.load("risk_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    amount = float(request.form["amount"])
    time = float(request.form["time"])
    user = float(request.form["user"])

    # Create 30 features (model expects 30)
    features = [0] * 30

    features[0] = amount
    features[1] = time

    # Generate behavior patterns
    features[2] = amount / 100
    features[3] = amount * 0.5
    features[4] = time / 10
    features[5] = user % 10
    features[6] = amount * time / 1000
    features[7] = amount / (time + 1)

    # Add variability
    for i in range(8, 30):
        features[i] = random.uniform(-2, 2)

    # Model prediction
    prediction = model.predict([features])
    probability = model.predict_proba([features])[0][1] * 100

    print("Fraud probability:", probability)

    # Decision logic
    if probability > 50:
        result = "⚠ Fraudulent Transaction"
        color = "red"
    else:
        result = "✅ Safe Transaction"
        color = "green"

    return render_template(
        "index.html",
        prediction_text=result,
        prob=round(probability, 2),
        color=color
    )


if __name__ == "__main__":
>>>>>>> 15e5a831f6b6473d9a1057145be1d94b03195951
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
from model import predict_risk

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == '1234':
            return redirect('/dashboard')
        return render_template('login.html', error="Invalid Credentials")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('index.html', result="", risk=0)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_id = request.form.get('userId')
        amount = float(request.form.get('amount') or 0)
        time_value = request.form.get('time')
        failed_attempts = int(request.form.get('failed_attempts') or 0)
        is_new_device = int(request.form.get('is_new_device') or 0)
        avg_amount = float(request.form.get('avg_amount') or 0)

        # Time mapping
        hour = 10 if time_value == "0" else 18 if time_value == "1" else 23

        pred, risk = predict_risk(amount, hour, failed_attempts, is_new_device, avg_amount)

        risk = max(0, min(round(risk * 100, 2), 100))

        result = "⚠ Fraud Detected" if pred == 1 else "✔ Safe Transaction"

        return render_template(
            'index.html',
            result=result,
            risk=risk,
            userId=user_id
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
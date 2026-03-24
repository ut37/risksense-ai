from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("LOGIN:", username, password)

        if username == 'admin' and password == '1234':
            return redirect('/welcome')   # first go to welcome page
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# WELCOME PAGE
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# DASHBOARD (RiskSense AI page)
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
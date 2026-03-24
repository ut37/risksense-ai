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
    app.run(debug=True)
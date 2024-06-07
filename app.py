from flask import Flask, request, render_template, redirect, url_for, session, flash
import builtwith
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = {'password': generate_password_hash(password)}
            flash('Registration successful, please log in')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    result = None
    if request.method == 'POST':
        url = request.form['url']
        website = builtwith.parse(url)
        result = {key: ", ".join(value) for key, value in website.items()}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

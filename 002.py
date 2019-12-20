from flask import Flask
from flask import url_for,escape

app = Flask(__name__)

@app.route('/')
def index():
    return "index"


@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


# app.run(port=5000,debug=True)
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
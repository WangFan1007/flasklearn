from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"


app.run('0.0.0.0',5000,debug=True)
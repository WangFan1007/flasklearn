from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/me_api')
def me():
    return {'name': '王凡', 'age': 30, 'salury': 10000}


@app.route('/members_api')
def members():
    return jsonify([{'name': '王凡', 'age': 30, 'salury': 10000}, {'name': '新新', 'age': 27, 'salury': 15000}])


app.run(port=5000, debug=True)

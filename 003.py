from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello',methods=['post','get'])
def hello():
    if request.method == 'POST':
        return 'post'
    elif request.method == 'GET':
        return 'get'


app.run(port=5000,debug=True)
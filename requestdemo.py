from flask import Flask,request


app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def index():

    print(request.data)
    
    return "{}".format(request.data)

if __name__ == '__main__':
    app.run(debug=True)
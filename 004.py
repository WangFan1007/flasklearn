from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/template')
def test():
    return render_template('test.html', data={"name": "王凡", "age": "30"})


app.run(debug=True, port=5000)

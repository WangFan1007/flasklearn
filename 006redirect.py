from flask import Flask, redirect, abort, url_for, render_template


app = Flask(__name__)


@app.route('/index')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(404)


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


app.run(port=5000, debug=True)

from flask import Flask, session, request, redirect, url_for, escape

app = Flask(__name__)
app.secret_key = 'ewgwgwjwjpjo'


@app.route('/')
def index():
    if 'username' in session:
        return 'logged in as {}'.format(escape(session['username']))
    return 'You are not logged in'


@app.route('/login', methods=['post', 'get'])
def login():
    print(request.method)
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method='post'>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


app.run(port=5000, debug=True)

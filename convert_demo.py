from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class RegxConverter(BaseConverter):
    def __init__(self, url_map, re):
        super().__init__(url_map)
        self.regex = re


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'

    def to_url(self, value):
        return "15183936364"

    def to_python(self, value):
        return "18912345678"


app.url_map.converters['re'] = RegxConverter
app.url_map.converters['mo'] = MobileConverter

@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    return 'SMS sended to {}'.format(mobile)


@app.route("/send2/<mo:mobile>")
def send2_sms(mobile):
    return 'SMS sended 2 {}'.format(mobile)

@app.route("/index")
def index():
    url = url_for("send2_sms",mobile="15928455943")
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, make_response
from requests import request

app = Flask(__name__)

# def return_cookies(request):
#   return request.cookies.get_dict()

@app.route('/', methods=["GET"])
def index():
  # req = request.get("https://www.google.com/")
  # print(return_cookies(req))
  return render_template('index.html')

@app.route('/logs/', methods=["GET"])
def show_logs():
  return render_template('logs.html')

@app.route('/cookie/', methods=["GET"])
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res
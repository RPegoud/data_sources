from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import requests

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  return render_template('index.html')

@app.route('/logs/', methods=["GET"])
def show_logs():
  return render_template('logs.html')

@app.route('/cookie/', methods=["GET"])
def cookie(): 
    if not request.cookies.get('google'):
        res = make_response("Setting a cookie")
        req = str(requests.request(url="https://www.google.com/", method='GET').cookies.get_dict())
        res.set_cookie('google', req, max_age=60*60*24*365*2)
    else:
        res = make_response(f"Value of cookie: {request.cookies.get('google')}")
    return res

     # https://analytics.google.com/analytics/web/#/p344199140/reports/intelligenthome
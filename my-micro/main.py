from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import requests

app = Flask(__name__)
g_analytics_url = 'https://analytics.google.com/analytics/web/#/p344199140/reports/intelligenthome'

@app.route('/', methods=["GET"])
def index():
  return render_template('index.html')

@app.route('/logs/', methods=["GET"])
def show_logs():
  return render_template('logs.html')

@app.route('/cookie/', methods=["GET"])
def cookie(): 
      # create and print a cookie
      # if not request.cookies.get('google_analytics'):
      #     res = make_response("Setting a cookie")
      #     # req = str(requests.request(url=g_analytics_url, method='GET'))
      #     req = requests.get(g_analytics_url).text
      #     res.set_cookie('google_analytics', req, max_age=60*60*24*365*2)
      # else:
      #     res = make_response(f"Value of cookie: {request.cookies.get('google_analytics')}")
      # return res
    return requests.get(g_analytics_url).text 


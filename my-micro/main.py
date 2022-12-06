from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
 return render_template('index.html')

@app.route('/logs/', methods=["GET"])
def show_logs():
  
  return render_template('logs.html')

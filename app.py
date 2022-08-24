from flask import Flask, jsonify
from datetime import datetime
import pytz
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World<h1>"

@app.route('/time', methods=['GET'])
def time():
    datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
    return datetime_india.strftime('%Y:%m:%d %H:%M:%S %Z %z')

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
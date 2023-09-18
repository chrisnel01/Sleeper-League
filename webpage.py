from flask import Flask, render_template
import json
import time

app = Flask(__name__)

with open("rosters.json", "r") as json_file:
    data = json.load(json_file)

# Record the time when the Flask application starts
last_run_time = time.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html', data=data, last_run_time=last_run_time)

if __name__ == '__main__':
    app.run(debug=True)

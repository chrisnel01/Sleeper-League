from flask import Flask, render_template
import json
from datetime import datetime, timedelta

app = Flask(__name__)

with open("rosters.json", "r") as json_file:
    data = json.load(json_file)

# Record the time when the Flask application starts
current_time = datetime.now()
adjusted_time = current_time - timedelta(hours=4)  # Subtract 4 hours
last_run_time = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html', data=data, last_run_time=last_run_time)

if __name__ == '__main__':
    app.run(debug=True)

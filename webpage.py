from flask import Flask, render_template
import json
from datetime import datetime, timedelta

app = Flask(__name__)

with open("rosters.json", "r") as json_file:
    data = json.load(json_file)

last_timestamp = "N/A"

with open("log.json", "r") as log_file:
            log_data = json.load(log_file)
            if log_data:
                last_entry = log_data[-1]  # Get the last entry in the log
                timestamp_str = last_entry.get("timestamp", "")
                if timestamp_str:
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    last_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    
@app.route('/')
def index():
    return render_template('index.html', data=data, last_timestamp=last_timestamp)

if __name__ == '__main__':
    app.run(debug=True)

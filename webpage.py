from flask import Flask, render_template

import json

app = Flask(__name__)

with open("rosters.json", "r") as json_file:
    data = json.load(json_file)


@app.route('/')
def index():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

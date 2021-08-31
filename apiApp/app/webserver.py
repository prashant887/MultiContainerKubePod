from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    msg = "Hello Python - {}".format(dt)
    return jsonify(msg), 200


app.run(host='0.0.0.0', port=8080, debug=True)

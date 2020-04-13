from flask import Flask, request, jsonify, request
from estimator import estimator
from data import data

app = Flask(__name__)

@app.route("/api/v1/on-covid-19", methods=["GET"])
def defualt_api():
    return jsonify(estimator(data))

@app.route("/", methods=["POST", "GET"])
def index():
    #return ("Hello")

if __name__=="__main__":
    app.run(debug=True)
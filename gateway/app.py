from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Use service name instead of localhost!
    response = requests.get('http://hello_service:5001/hello')
    return jsonify(response.json())

@app.route('/greet/<name>')
def greet(name):
    response = requests.get(f'http://greet_service:5002/greet/{name}')
    return jsonify(response.json())

@app.route('/fact')
def fact():
    response = requests.get('http://fact_service:5003/fact')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
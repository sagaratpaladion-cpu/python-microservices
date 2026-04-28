from flask import Flask, jsonify
import requests   # Install this: pip install requests

app = Flask(__name__)

# Forward to Hello Service
@app.route('/hello')
def hello():
    response = requests.get('http://localhost:5001/hello')
    return jsonify(response.json())

# Forward to Greet Service
@app.route('/greet/<name>')
def greet(name):
    response = requests.get(f'http://localhost:5002/greet/{name}')
    return jsonify(response.json())

# Forward to Fact Service
@app.route('/fact')
def fact():
    response = requests.get('http://localhost:5003/fact')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)   # The only port users need to know!
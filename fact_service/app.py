from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fact')
def fact():
    return jsonify({ "fact": "Python was named after Monty Python! 🐍" })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)  # Another different port!
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return jsonify({ "message": f"Hey {name}, welcome! 👋" })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Different port!
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    return jsonify(status='UP')

if __name__ == '__main__':
    app.run(debug=True)
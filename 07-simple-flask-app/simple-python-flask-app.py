from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/about')
def about():
    return "This is the about page!"

@app.route('/health')
def health():
    return "OK"

@app.route('/mock_api', methods=['GET'])
def mock_api():
    try:
        return jsonify({"message": "Mocked API Response", "status": "Success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Pipeline Running", "job": "Build #23"})

if __name__ == '__main__':
    app.run()
    # The host='0.0.0.0' argument allows the Flask app to be accessible from your Windows machine via your local network.
    # app.run(host='0.0.0.0')

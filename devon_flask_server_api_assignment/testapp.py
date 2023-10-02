from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=["POST"])
def process_request():
    # Get the request data as JSON
    data = request.get_json()

    # Check if 'prompt' and 'user' are present in the request JSON
    if 'prompt' in data and 'user' in data:
        return jsonify({"status": "Success", "message": "Request processed successfully"}), 200
    else:
        return jsonify({"status": "Error", "message": "'prompt' and 'user' parameters are required"}), 400

if __name__ == '__main__':
    app.run(port=8080)

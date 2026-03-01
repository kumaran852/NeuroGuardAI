from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from NeuroGuardAI!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    text = data.get('text', '')
    score = len(set(text.split())) / len(text.split()) * 100 if text else 0
    return jsonify({'score': round(score, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

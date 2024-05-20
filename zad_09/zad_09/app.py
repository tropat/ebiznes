from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    messages = [
        {
            'role': 'user',
            'content': user_input,
        },
    ]

    response = ollama.chat(model='llama2', messages=messages)

    if 'message' not in response or 'content' not in response['message']:
        return jsonify({"error": "Invalid response from LLAMA model"}), 500

    return jsonify({"response": response['message']['content']})


if __name__ == '__main__':
    app.run(port=8000)

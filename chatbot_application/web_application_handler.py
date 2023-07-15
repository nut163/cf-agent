```python
from flask import Flask, request, jsonify
from chatbot import Chatbot
from user_input_handler import handleUserInput
from code_updater import updateExistingCode
from file_upload_handler import uploadFile

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/user-input', methods=['POST'])
def receiveUserInput():
    user_prompt = request.json.get('user_prompt')
    response = handleUserInput(user_prompt)
    return jsonify(response)

@app.route('/update-code', methods=['POST'])
def updateCode():
    existing_code = request.files['existing_code']
    code_path = uploadFile(existing_code)
    response = updateExistingCode(code_path)
    return jsonify(response)

@app.route('/generate-code', methods=['POST'])
def generateColdFusionCode():
    user_prompt = request.json.get('user_prompt')
    response = chatbot.generate_code(user_prompt)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
```
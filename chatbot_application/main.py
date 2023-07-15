```python
from chatbot import Chatbot
from user_input_handler import UserInputHandler
from file_upload_handler import FileUploadHandler

def main():
    chatbot = Chatbot()
    user_input_handler = UserInputHandler()
    file_upload_handler = FileUploadHandler()

    while True:
        user_prompt = user_input_handler.handleUserInput()
        if user_prompt == "quit":
            break

        if user_prompt == "upload":
            existing_code = file_upload_handler.uploadFile()
            chatbot.updateExistingCode(existing_code)
        else:
            chatbot.generateColdFusionCode(user_prompt)

if __name__ == "__main__":
    main()
```
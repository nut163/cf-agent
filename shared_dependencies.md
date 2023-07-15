Shared Dependencies:

1. Variables:
   - `user_prompt`: This variable will store the user's intent or what they want to do.
   - `existing_code`: This variable will store the existing code that needs to be updated.

2. Data Schemas:
   - `UserInput`: This schema will define the structure of the user's input, including `user_prompt` and `existing_code`.

3. ID Names of DOM Elements:
   - `userPromptInput`: This is the ID of the input field where the user enters their prompt.
   - `codeUploadButton`: This is the ID of the button that allows the user to upload their existing code.

4. Message Names:
   - `receiveUserInput`: This message is sent when the user submits their input.
   - `updateCode`: This message is sent when the user uploads their existing code.

5. Function Names:
   - `handleUserInput(user_prompt)`: This function handles the user's prompt.
   - `updateExistingCode(existing_code)`: This function updates the existing code with the user's changes.
   - `uploadFile()`: This function handles the file upload process.
   - `generateColdFusionCode(user_prompt)`: This function generates ColdFusion code based on the user's prompt.
   - `handleWebApplication()`: This function handles the creation and management of the web application.
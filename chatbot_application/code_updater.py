```python
import os

class CodeUpdater:
    def __init__(self):
        self.existing_code = None

    def upload_file(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                self.existing_code = file.read()
        else:
            raise Exception("File does not exist")

    def update_existing_code(self, updated_code):
        if self.existing_code is not None:
            self.existing_code = updated_code
        else:
            raise Exception("No existing code to update")

    def save_updated_code(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.existing_code)
```
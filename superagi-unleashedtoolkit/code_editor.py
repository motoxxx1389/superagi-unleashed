class CodeEditor:
    def __init__(self):
        self.code = ""

    def input_code(self):
        self.code = input("Enter your code: ")

    def upload_file(self, file_path):
        with open(file_path, 'r') as file:
            self.code = file.read()

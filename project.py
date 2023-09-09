class Project:
    def __init__(self, name: str):
        self.name = name
        self.code_files = []
        self.exe_file = None
        self.installer = None

    def add_code_file(self, file_path: str):
        self.code_files.append(file_path)

    def compile(self):
        # Implementation of compile method goes here

    def package_with_installer(self):
        # Implementation of package_with_installer method goes here

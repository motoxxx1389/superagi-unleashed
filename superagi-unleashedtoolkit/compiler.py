import subprocess

class Compiler:
    def __init__(self, code):
        self.code = code

    def compile_code(self):
        # Save the code to a temporary Python file
        with open('temp.py', 'w') as file:
            file.write(self.code)

        # Use PyInstaller to compile the code into a .exe application
        subprocess.run(['pyinstaller', '--onefile', 'temp.py'])

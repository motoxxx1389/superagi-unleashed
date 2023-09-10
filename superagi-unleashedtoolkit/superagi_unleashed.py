from code_editor import CodeEditor
from compiler import Compiler
from packager import Packager

class SuperAGIUnleashed:
    def __init__(self):
        self.code_editor = CodeEditor()
        self.compiler = None
        self.packager = None

    def run(self):
        # Get the code from the user
        self.code_editor.input_code()

        # Compile the code into a .exe application
        self.compiler = Compiler(self.code_editor.code)
        self.compiler.compile_code()

        # Package the .exe application into an installer
        self.packager = Packager('dist/temp.exe')
        self.packager.package_exe()

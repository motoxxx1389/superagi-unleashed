import subprocess

class Packager:
    def __init__(self, exe_path):
        self.exe_path = exe_path

    def package_exe(self):
        # Use Inno Setup to package the .exe application into an installer
        subprocess.run(['Inno Setup command line', self.exe_path])

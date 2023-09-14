import subprocess

class ApplicationBuilder:
    def __init__(self):
        self.app_name = None
        self.app_version = None
        self.app_description = None
        self.resources = []

    def set_properties(self, app_name, app_version, app_description):
        self.app_name = app_name
        self.app_version = app_version
        self.app_description = app_description

    def add_resources(self, resource_files):
        self.resources.extend(resource_files)

    def compile_to_exe(self, input_file):
        cmd = [
            'pyinstaller',
            '--name={}'.format(self.app_name),
            '--version-file={}'.format(self.app_version),
            # Add other options as needed
            input_file
        ]
        subprocess.run(cmd)


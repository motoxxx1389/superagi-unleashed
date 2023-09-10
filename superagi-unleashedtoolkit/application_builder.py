from pyinstaller import Executable

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

    def compile_to_exe(self, input_files, output_file):
        exe = Executable(
            script=input_files,
            name=self.app_name,
            version=self.app_version,
            description=self.app_description,
            resources=self.resources
        )
        exe.compile(output_file)

from project import Project
from compiler import Compiler
from installer_packager import InstallerPackager

class AgentInterface:
    def __init__(self):
        self.projects = {}
        self.compiler = Compiler()
        self.installer_packager = InstallerPackager()

    def create_project(self, name: str):
        self.projects[name] = Project(name)

    def add_code_file(self, project_name: str, file_path: str):
        self.projects[project_name].add_code_file(file_path)

    def compile_project(self, project_name: str):
        self.compiler.compile(self.projects[project_name])

    def package_with_installer(self, project_name: str):
        self.installer_packager.package(self.projects[project_name])

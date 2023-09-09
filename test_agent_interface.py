import unittest
from superagi_toolkit import AgentInterface, Project, Compiler, InstallerPackager

class TestAgentInterface(unittest.TestCase):
    def setUp(self):
        self.agent_interface = AgentInterface()
        self.project_name = 'test_project'
        self.file_path = 'test_file.py'

    def test_create_project(self):
        self.agent_interface.create_project(self.project_name)
        self.assertIn(self.project_name, self.agent_interface.projects)

    def test_add_code_file(self):
        self.agent_interface.create_project(self.project_name)
        self.agent_interface.add_code_file(self.project_name, self.file_path)
        self.assertIn(self.file_path, self.agent_interface.projects[self.project_name].code_files)

    def test_compile_project(self):
        self.agent_interface.create_project(self.project_name)
        self.agent_interface.add_code_file(self.project_name, self.file_path)
        self.agent_interface.compile_project(self.project_name)
        self.assertIsNotNone(self.agent_interface.projects[self.project_name].exe_file)

    def test_package_with_installer(self):
        self.agent_interface.create_project(self.project_name)
        self.agent_interface.add_code_file(self.project_name, self.file_path)
        self.agent_interface.compile_project(self.project_name)
        self.agent_interface.package_with_installer(self.project_name)
        self.assertIsNotNone(self.agent_interface.projects[self.project_name].installer)

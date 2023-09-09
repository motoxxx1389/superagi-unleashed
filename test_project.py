import unittest
from superagi_toolkit import Project

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project('test_project')
        self.file_path = 'test_file.py'

    def test_add_code_file(self):
        self.project.add_code_file(self.file_path)
        self.assertIn(self.file_path, self.project.code_files)

    def test_compile(self):
        self.project.add_code_file(self.file_path)
        self.project.compile()
        self.assertIsNotNone(self.project.exe_file)

    def test_package_with_installer(self):
        self.project.add_code_file(self.file_path)
        self.project.compile()
        self.project.package_with_installer()
        self.assertIsNotNone(self.project.installer)

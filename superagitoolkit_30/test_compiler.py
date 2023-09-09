import unittest
from superagi_toolkit import Compiler, Project

class TestCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = Compiler()
        self.project = Project('test_project')
        self.project.add_code_file('test_file.py')

    def test_compile(self):
        self.compiler.compile(self.project)
        self.assertIsNotNone(self.project.exe_file)

import unittest
from superagi_toolkit import InstallerPackager, Project

class TestInstallerPackager(unittest.TestCase):
    def setUp(self):
        self.installer_packager = InstallerPackager()
        self.project = Project('test_project')
        self.project.add_code_file('test_file.py')
        self.project.compile()

    def test_package(self):
        self.installer_packager.package(self.project)
        self.assertIsNotNone(self.project.installer)

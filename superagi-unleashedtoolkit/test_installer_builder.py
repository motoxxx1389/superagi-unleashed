import unittest
from superagi_unleashed import InstallerBuilder

class TestInstallerBuilder(unittest.TestCase):
    def setUp(self):
        self.installer_builder = InstallerBuilder()

    def test_create_installer(self):
        installer_file = self.installer_builder.create_installer('test.exe', 'installer.exe')
        self.assertTrue(os.path.isfile(installer_file))

if __name__ == '__main__':
    unittest.main()

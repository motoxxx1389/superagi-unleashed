import unittest
from superagi_unleashed import ApplicationBuilder

class TestApplicationBuilder(unittest.TestCase):
    def setUp(self):
        self.app_builder = ApplicationBuilder()

    def test_set_properties(self):
        self.app_builder.set_properties('Test App', '1.0', 'This is a test application')
        self.assertEqual(self.app_builder.app_name, 'Test App')
        self.assertEqual(self.app_builder.app_version, '1.0')
        self.assertEqual(self.app_builder.app_description, 'This is a test application')

    def test_add_resources(self):
        self.app_builder.add_resources(['test.png', 'test.wav'])
        self.assertEqual(self.app_builder.resource_files, ['test.png', 'test.wav'])

if __name__ == '__main__':
    unittest.main()

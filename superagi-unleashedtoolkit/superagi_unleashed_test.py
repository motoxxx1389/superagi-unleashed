import unittest
from superagi_unleashed import CodeEditor, Compiler, Packager, SuperAGIUnleashed

class TestSuperAGIUnleashed(unittest.TestCase):

    def setUp(self):
        self.superagi = SuperAGIUnleashed()

    def test_code_editor(self):
        self.assertIsInstance(self.superagi.code_editor, CodeEditor)
        code = "print('Hello, World!')"
        self.superagi.code_editor.type_code(code)
        self.assertEqual(self.superagi.code_editor.code, code)
        self.superagi.code_editor.upload_code("test_code.py")
        with open("test_code.py", 'r') as file:
            uploaded_code = file.read()
        self.assertEqual(self.superagi.code_editor.code, uploaded_code)

    def test_compiler(self):
        self.assertIsInstance(self.superagi.compiler, Compiler)
        self.superagi.code_editor.type_code("print('Hello, World!')")
        self.superagi.compiler.compile(self.superagi.code_editor.code)
        self.assertTrue(os.path.exists(self.superagi.compiler.exe_path))

    def test_packager(self):
        self.assertIsInstance(self.superagi.packager, Packager)
        self.superagi.code_editor.type_code("print('Hello, World!')")
        self.superagi.compiler.compile(self.superagi.code_editor.code)
        self.superagi.packager.package(self.superagi.compiler.exe_path)
        self.assertTrue(os.path.exists(self.superagi.packager.installer_path))

    def test_superagi_unleashed(self):
        self.assertIsInstance(self.superagi, SuperAGIUnleashed)
        self.superagi.create_exe_and_installer("print('Hello, World!')")
        self.assertTrue(os.path.exists(self.superagi.compiler.exe_path))
        self.assertTrue(os.path.exists(self.superagi.packager.installer_path))

if __name__ == "__main__":
    unittest.main()

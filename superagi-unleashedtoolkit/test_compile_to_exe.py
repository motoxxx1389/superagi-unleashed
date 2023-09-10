import unittest
from superagi_unleashed import compile_to_exe

class TestCompileToExe(unittest.TestCase):
    def test_compile_to_exe(self):
        output_file = compile_to_exe(['test.py'], 'test.exe')
        self.assertTrue(os.path.isfile(output_file))

if __name__ == '__main__':
    unittest.main()

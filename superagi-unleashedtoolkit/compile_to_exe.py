from PyInstaller import __main__ as pyi

def compile_to_exe(input_files, output_file):
    pyi.run(['--name=%s' % output_file, '--onefile'] + input_files)

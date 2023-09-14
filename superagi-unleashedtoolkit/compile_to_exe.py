from PyInstaller.__main__ import run as pyi_run

def compile_to_exe(input_files, output_file):
    """
    Compiles the given input files into an executable using PyInstaller.

    :param input_files: A single file (str) or a list of files to compile.
    :param output_file: The name of the output executable.
    """
    # Ensure input_files is a list
    if not isinstance(input_files, list):
        input_files = [input_files]

    # Construct the PyInstaller command
    cmd = ['--name={}'.format(output_file), '--onefile'] + input_files

    try:
        pyi_run(cmd)
    except Exception as e:
        print(f"Error during compilation: {e}")

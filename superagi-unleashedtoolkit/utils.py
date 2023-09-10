from application_builder import ApplicationBuilder
from installer_builder import InstallerBuilder

def compile_to_exe(input_files, output_file, app_name, app_version, app_description):
    builder = ApplicationBuilder(app_name, app_version, app_description)
    builder.compile_to_exe(input_files, output_file)

def create_installer(app_exe, installer_name):
    builder = InstallerBuilder(installer_name)
    builder.create_installer(app_exe)

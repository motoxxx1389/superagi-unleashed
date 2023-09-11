from innosetup import Script

class InstallerBuilder:
    def __init__(self):
        self.installer_name = None
        self.app_exe = None

    def set_properties(self, app_exe, installer_name):
        self.app_exe = app_exe
        self.installer_name = installer_name

    def create_installer(self):
        script = Script(
            app_exe=self.app_exe,
            installer_name=self.installer_name
        )
        script.compile()

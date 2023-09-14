import os

def create_installer(app_exe, installer_name):
    script = f"""
    [Setup]
    AppName={installer_name}
    AppVerName={installer_name}
    DefaultDirName={app_exe}
    OutputBaseFilename={installer_name}
    Compression=lzma
    SolidCompression=yes
    """

    with open("installer_script.iss", "w") as f:
        f.write(script)

    os.system(f'iscc installer_script.iss')


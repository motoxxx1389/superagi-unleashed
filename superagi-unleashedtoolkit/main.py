from application_builder import ApplicationBuilder
from installer_builder import InstallerBuilder

def main():
    app_builder = ApplicationBuilder()
    app_builder.set_properties('MyApp', '1.0.0', 'My first application')
    app_builder.add_resources(['image.png', 'sound.wav'])
    app_builder.compile_to_exe('main.py', 'MyApp.exe')

    installer_builder = InstallerBuilder()
    installer_builder.set_properties('MyApp.exe', 'MyAppInstaller')
    installer_builder.create_installer()

if __name__ == "__main__":
    main()

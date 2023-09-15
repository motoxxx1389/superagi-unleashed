#!/bin/bash

# Overview:
# This script provides an outline for creating standalone `.exe` applications and their respective installers.

# Classes:

# 1. ApplicationBuilder
# Purpose: Handles the creation of the `.exe` application.
# Key Methods:
# - set_properties(app_name, app_version, app_description): Sets the application's metadata.
# - add_resources(resource_files): Embeds resource files like images and sounds into the application.

# 2. InstallerBuilder
# Purpose: Manages the creation of an installer for the `.exe` application.
# Key Methods:
# - set_properties(app_exe, installer_name): Sets the properties for the installer.

# Functions:

# 1. compile_to_exe(input_files, output_file)
# Purpose: Compiles input files into a single `.exe` file using PyInstaller or cx_Freeze.

# 2. create_installer(app_exe, installer_name)
# Purpose: Creates an installer for the `.exe` application using Inno Setup or NSIS.

# Installation Notes:

# If superagi-unleashed doesn't install all the requirements, follow these steps:
# 1. Wait until the build is complete.
# 2. Shut down the service: `docker-compose down`
# 3. Clone the necessary repository: `git clone https://github.com/idleberg/vscode-innosetup innosetup`
# 4. Restart the service: `docker-compose up --build`

# Manual Installation:
# - You might need to manually install PyInstaller and Inno-Setup.
# - If there's a path error, download the tool and add its path to your environment variables.

# PyInstaller on Python: https://pypi.org/project/pyinstaller/
# Inno-Setup GitHub Repo: https://github.com/jrsoftware/issrc


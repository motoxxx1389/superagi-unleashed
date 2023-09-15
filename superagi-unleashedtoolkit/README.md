#!/bin/bash

# Overview:
# This script outlines the process of creating standalone `.exe` applications and their installers.

# Classes:

# 1. ApplicationBuilder
# - Purpose: Facilitates the creation of `.exe` applications.
# - set_properties(app_name, app_version, app_description): Defines the application's metadata.
# - add_resources(resource_files): Incorporates resources like images and sounds into the application.

# 2. InstallerBuilder
# - Purpose: Oversees the creation of an installer for the `.exe` application.
# - set_properties(app_exe, installer_name): Defines the installer's properties.

# Functions:

# 1. compile_to_exe(input_files, output_file)
# - Purpose: Transforms input files into a singular `.exe` file, utilizing PyInstaller or cx_Freeze.

# 2. create_installer(app_exe, installer_name)
# - Purpose: Generates an installer for the `.exe` application, leveraging Inno Setup or NSIS.

# Installation Guidance:

# For superagi-unleashed:
# 1. Allow the build to complete fully.
# 2. Terminate the service using: `docker-compose down`
# 3. Procure the required modules from the links provided below.
# 4. Reactivate the service with: `docker-compose up --build`

# Manual Installation Tips:
# - PyInstaller and Inno-Setup might necessitate manual installation.
# - In case of a path discrepancy, retrieve the tool and incorporate its path into your environment variables.

# Relevant Links:
# - PyInstaller: https://pypi.org/project/pyinstaller/
# - Inno-Setup: https://pypi.org/project/innosetup/

# ==============================
# 1. PIP (PYTHON PACKAGE MANAGER)
# ==============================

# pip is the official Python package manager
#
# It is used to:
# - install packages
# - update packages
# - remove packages
# - manage external Python libraries


# -------------------------
# CHECK PIP VERSION
# -------------------------

# Show the installed pip version
#
# Command in terminal:
# pip --version

# Example:
# pip 25.0 from ...
# python version ...


# -------------------------
# INSTALL A PACKAGE
# -------------------------

# Install a package from PyPI
#
# Syntax:
# pip install package_name
#
# Example:
# pip install requests


# -------------------------
# INSTALL A SPECIFIC VERSION
# -------------------------

# Install a specific package version
#
# Syntax:
# pip install package_name==version
#
# Example:
# pip install django==5.0


# -------------------------
# VERSION RANGE EXAMPLES
# -------------------------

# Install a compatible version using "~="
#
# "~=" means:
# Install the latest compatible version
# without changing the major/minor version
#
# Example:
# pip install django~=2.9.0
#
# This allows:
# - 2.9.0
# - 2.9.1
# - 2.9.5
#
# But NOT:
# - 2.10.0
# - 3.0.0
#
# It is approximately equivalent to:
# >=2.9.0 and <2.10.0


# Install versions using "*"
#
# Example:
# pip install django==2.9.*
#
# This means:
# install ANY version starting with 2.9
#
# Allowed:
# - 2.9.0
# - 2.9.1
# - 2.9.8
#
# Not allowed:
# - 2.10.0
# - 3.0.0


# -------------------------
# UPDATE A PACKAGE
# -------------------------

# Upgrade an installed package
#
# Syntax:
# pip install --upgrade package_name
#
# Example:
# pip install --upgrade requests


# -------------------------
# REMOVE A PACKAGE
# -------------------------

# Uninstall a package
#
# Syntax:
# pip uninstall package_name
#
# Example:
# pip uninstall requests


# -------------------------
# LIST INSTALLED PACKAGES
# -------------------------

# Show all installed packages
#
# Command:
# pip list


# -------------------------
# SHOW PACKAGE INFORMATION
# -------------------------

# Display details about a package
#
# Command:
# pip show requests


# -------------------------
# SAVE DEPENDENCIES
# -------------------------

# Save installed packages into requirements.txt
#
# Useful for projects
#
# Command:
# pip freeze > requirements.txt


# -------------------------
# INSTALL FROM requirements.txt
# -------------------------

# Install all packages listed in requirements.txt
#
# Command:
# pip install -r requirements.txt


# -------------------------
# INSTALL PACKAGE FOR USER ONLY
# -------------------------

# Install package only for the current user
#
# Command:
# pip install --user package_name


# -------------------------
# COMMON ISSUE
# -------------------------

# If "pip" does not work,
# try using:
#
# python -m pip install package_name
#
# Example:
# python -m pip install requests


import requests


# Send an HTTP GET request to Google
#
# requests.get(url)
# → sends a GET request to the specified URL
response = requests.get("http://google.com")


# Print the response object
#
# Example output:
# <Response [200]>
#
# 200 means:
# the request was successful
print(response)


# -------------------------
# USEFUL RESPONSE DATA
# -------------------------

# Print the HTTP status code
# Example: 200, 404, 500 ...
print(response.status_code)


# ==============================
# 2. VIRTUAL ENVIRONMENT (venv)
# ==============================

# A Virtual Environment is an isolated Python environment
#
# It allows each project to have:
# - its own packages
# - its own dependencies
# - its own package versions
#
# This avoids conflicts between projects


# -------------------------
# CREATE A VIRTUAL ENVIRONMENT
# -------------------------

# Syntax:
# python -m venv folder_name
#
# Example:
# python -m venv env

# This creates a folder named "env"
# containing:
# - a private Python interpreter
# - pip
# - installed packages


# -------------------------
# ACTIVATE THE ENVIRONMENT
# -------------------------

# WINDOWS (Command Prompt)
# env\Scripts\activate

# WINDOWS (PowerShell)
# .\env\Scripts\Activate.ps1

# LINUX / MAC
# source env/bin/activate


# -------------------------
# AFTER ACTIVATION
# -------------------------

# The terminal usually changes like this:
#
# (env) C:\project>
#
# Meaning:
# the virtual environment is active


# -------------------------
# INSTALL PACKAGES INSIDE ENV
# -------------------------

# Example:
# pip install requests

# The package will be installed ONLY
# inside this virtual environment


# -------------------------
# CHECK INSTALLED PACKAGES
# -------------------------

# Show installed packages
#
# Command:
# pip list


# -------------------------
# SAVE PROJECT DEPENDENCIES
# -------------------------

# Save all installed packages into requirements.txt
#
# Command:
# pip freeze > requirements.txt


# -------------------------
# INSTALL DEPENDENCIES
# -------------------------

# Install packages from requirements.txt
#
# Command:
# pip install -r requirements.txt


# -------------------------
# DEACTIVATE THE ENVIRONMENT
# -------------------------

# Exit the virtual environment
#
# Command:
# deactivate


# -------------------------
# IMPORTANT
# -------------------------

# Usually, the virtual environment folder
# (env or venv) is NOT uploaded to GitHub
#
# Instead:
# - upload requirements.txt
# - recreate the environment later

# ==============================
# 3. PIPENV
# ==============================

# pipenv is a tool that combines:
# - pip
# - virtual environments
#
# It automatically:
# - creates virtual environments
# - manages dependencies
# - manages Pipfile and Pipfile.lock
#
# pipenv is an alternative to:
# - venv
# - requirements.txt


# -------------------------
# INSTALL PIPENV
# -------------------------

# Install pipenv globally
#
# Command:
# pip install pipenv


# -------------------------
# INSTALL A PACKAGE
# -------------------------

# Install a package and create a virtual environment
#
# Example:
# pipenv install requests

# This automatically:
# - creates a virtual environment
# - installs requests
# - creates Pipfile
# - creates Pipfile.lock


# -------------------------
# PIPFILE
# -------------------------

# Pipfile stores:
# - project dependencies
# - Python version requirements
#
# Example:
#
# [packages]
# requests = "*"


# -------------------------
# PIPFILE.LOCK
# -------------------------

# Pipfile.lock stores:
# - exact package versions
# - dependency tree
#
# Used for reproducible installations


# -------------------------
# ACTIVATE THE ENVIRONMENT
# -------------------------

# Open the virtual environment shell
#
# Command:
# pipenv shell


# -------------------------
# RUN COMMANDS WITHOUT SHELL
# -------------------------

# Run Python inside pipenv environment
#
# Command:
# pipenv run python app.py


# -------------------------
# INSTALL DEVELOPMENT PACKAGES
# -------------------------

# Install packages used only for development
#
# Example:
# pipenv install pytest --dev


# -------------------------
# SHOW INSTALLED PACKAGES
# -------------------------

# Command:
# pipenv graph

# Shows dependency tree


# -------------------------
# REMOVE A PACKAGE
# -------------------------

# Example:
# pipenv uninstall requests


# -------------------------
# EXIT THE ENVIRONMENT
# -------------------------

# Command:
# exit


# -------------------------
# INSTALL FROM EXISTING Pipfile
# -------------------------

# Install all dependencies
#
# Command:
# pipenv install


# -------------------------
# CHECK VIRTUAL ENV LOCATION
# -------------------------

# Command:
# pipenv --venv


# -------------------------
# IMPORTANT NOTES
# -------------------------

# pipenv automatically manages:
# - virtual environments
# - package versions
#
# No need to manually create venv folders

# 4 v 5

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
# INSTALL FROM EXISTING Pipfile
# -------------------------

# Install all dependencies
#
# Command:
# pipenv install


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

# ==============================
# 4. VIRTUAL ENVIRONMENT IN VSCODE
# ==============================

# VSCode can automatically detect and use
# Python virtual environments
#
# This helps:
# - isolate project dependencies
# - use the correct Python interpreter
# - avoid package conflicts


# -------------------------
# SELECT PYTHON INTERPRETER
# -------------------------

# In VSCode:
#
# Press:
# Ctrl + Shift + P
#
# Search:
# Python: Select Interpreter
#
# Then choose:
# the interpreter inside your virtual environment
#
# Example path:
# ./env/Scripts/python.exe


# -------------------------
# VERIFY THE ENVIRONMENT
# -------------------------

# Open terminal in VSCode
#
# You should see:
#
# (env)
#
# before the terminal path
#
# Example:
# (env) C:\Projects\MyApp>


# -------------------------
# CODE RUNNER ISSUE
# -------------------------

# Sometimes VSCode Code Runner
# uses the WRONG Python interpreter
#
# To fix this:
#
# Open:
# settings.json
#
# Then modify:
#
# "code-runner.executorMap"
#
# Example:
#
# "python":
# "C:/Users/USERNAME/.virtualenvs/project-name/Scripts/python.exe -u"
#
# In your screenshot,
# VSCode is configured to use:
#
# C:/Users/makhl/.virtualenvs/Mosh_Tuto-SKIwAj01/bin/python -u
#
# This forces Code Runner
# to execute Python using the
# selected virtual environment


# -------------------------
# COMMON ISSUE
# -------------------------

# If VSCode does NOT detect the environment:
#
# 1. Restart VSCode
# 2. Reopen the project folder
# 3. Re-select the interpreter manually


# -------------------------
# USEFUL SHORTCUTS
# -------------------------

# Open terminal:
# Ctrl + `

# Open command palette:
# Ctrl + Shift + P

# ==============================
# 5. PIPFILE & PIPFILE.LOCK
# ==============================

# Pipfile and Pipfile.lock are used by pipenv
#
# They replace:
# - requirements.txt
# - manual virtual environment management
#
# These files help manage:
# - dependencies
# - package versions
# - Python version
# - reproducible environments


# -------------------------
# WHAT IS Pipfile ?
# -------------------------

# Pipfile stores:
# - project dependencies
# - Python version requirements
# - development packages
#
# It is human-readable


# Example Pipfile:
#
# [[source]]
# url = "https://pypi.org/simple"
# verify_ssl = true
# name = "pypi"
#
# [packages]
# requests = "*"
# django = "==5.0"
#
# [dev-packages]
# pytest = "*"
#
# [requires]
# python_version = "3.12"


# -------------------------
# WHAT IS Pipfile.lock ?
# -------------------------

# Pipfile.lock stores:
# - exact package versions
# - dependency tree
# - hashes for security
#
# It is automatically generated
#
# Example:
#
# requests==2.32.0
# urllib3==2.2.1
#
# This guarantees:
# everyone installs EXACTLY
# the same versions


# -------------------------
# CREATE Pipfile AUTOMATICALLY
# -------------------------

# Install a package using pipenv
#
# Example:
# pipenv install requests

# This automatically creates:
# - Pipfile
# - Pipfile.lock


# -------------------------
# INSTALL ALL DEPENDENCIES
# -------------------------

# Install packages from Pipfile.lock
#
# Command:
# pipenv install


# -------------------------
# ADD DEVELOPMENT PACKAGES
# -------------------------

# Example:
# pipenv install pytest --dev

# Stored under:
# [dev-packages]


# -------------------------
# UPDATE DEPENDENCIES
# -------------------------

# Update packages and lock file
#
# Command:
# pipenv update


# -------------------------
# REMOVE A PACKAGE
# -------------------------

# Example:
# pipenv uninstall requests


# -------------------------
# WHY Pipfile.lock IS IMPORTANT
# -------------------------

# Without Pipfile.lock:
# different developers may install
# different package versions
#
# With Pipfile.lock:
# everyone gets the SAME environment


# -------------------------
# IMPORTANT
# -------------------------

# Usually uploaded to GitHub:
# - Pipfile
# - Pipfile.lock
#
# Usually NOT uploaded:
# - virtual environment folder

# ==============================
# 6. MANAGING DEPENDENCIES WITH PIPENV
# ==============================

# pipenv helps manage:
# - project dependencies
# - package versions
# - virtual environments
#
# It automatically updates:
# - Pipfile
# - Pipfile.lock


# -------------------------
# INSTALL A PACKAGE
# -------------------------

# Example:
# pipenv install requests

# This:
# - installs requests
# - updates Pipfile
# - updates Pipfile.lock


# -------------------------
# INSTALL A SPECIFIC VERSION
# -------------------------

# Example:
# pipenv install requests==2.31.0

# Installs exactly version 2.31.0


# -------------------------
# VERSION PATTERNS
# -------------------------

# Inside Pipfile:
#
# [packages]
# requests = "==2.9.*"

# Meaning:
# install any version starting with 2.9
#
# Allowed:
# - 2.9.0
# - 2.9.1
# - 2.9.5
#
# Not allowed:
# - 2.10.0
# - 3.0.0


# Another example:
#
# requests = "~=2.9.0"
#
# Meaning:
# install compatible versions
#
# Equivalent to:
# >=2.9.0 and <2.10.0


# -------------------------
# SHOW INSTALLED PACKAGES
# -------------------------

# Display dependency tree
#
# Command:
# pipenv graph

# Example output:
#
# requests==2.31.0
# ├── certifi
# ├── charset-normalizer
# ├── idna
# └── urllib3


# -------------------------
# CHECK OUTDATED PACKAGES
# -------------------------

# Show packages that can be updated
#
# Command:
# pipenv update --outdated

# Displays:
# - current version
# - latest version


# -------------------------
# UPDATE ALL PACKAGES
# -------------------------

# Update dependencies
#
# Command:
# pipenv update

# Updates:
# - Pipfile.lock
# - installed packages


# -------------------------
# UPDATE A SINGLE PACKAGE
# -------------------------

# Example:
# pipenv update requests


# -------------------------
# REMOVE A PACKAGE
# -------------------------

# Example:
# pipenv uninstall requests


# -------------------------
# INSTALL DEVELOPMENT PACKAGES
# -------------------------

# Example:
# pipenv install pytest --dev

# Added under:
# [dev-packages]


# -------------------------
# INSTALL FROM Pipfile.lock
# -------------------------

# Reinstall exact dependency versions
#
# Command:
# pipenv install


# -------------------------
# VERIFY SECURITY ISSUES
# -------------------------

# Check for known vulnerabilities
#
# Command:
# pipenv check


# -------------------------
# IMPORTANT
# -------------------------

# Pipfile.lock guarantees:
# every developer installs
# the exact same dependency versions

# V 8

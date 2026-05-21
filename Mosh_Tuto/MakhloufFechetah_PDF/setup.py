# Import setuptools
#
# setuptools is used to create and publish Python packages
import setuptools

# Import Path from pathlib
#
# Used to read the README.md file
from pathlib import Path


# setup() contains package metadata
setuptools.setup(

    # Package name on PyPI
    #
    # IMPORTANT:
    # Must be UNIQUE on PyPI
    name="MakhloufFechetah_PDF",

    # Package author name
    author="Makhlouf",

    # Current package version
    version="1.0.0",

    # Long package description
    #
    # Reads the content of README.md
    # and displays it on the PyPI page
    long_description=Path("README.md").read_text(),

    # Automatically find all Python packages
    #
    # exclude=["tests", "data"]
    # prevents these folders from being packaged
    packages=setuptools.find_packages(
        exclude=["tests", "data"]
    )
)

#!/usr/bin/env python3

# File: setup.py
# Author: Hadi Cahyadi <cumulus13@gmail.com>
# Date: 2025-12-30
# Description: 
# License: MIT

# setup.py
from setuptools import setup, find_packages
from pathlib import Path
import os
import traceback
import shutil

NAME = 'pathlib3'

try:
    shutil.copy2("__version__.py", NAME)
except Exception:
    pass

# Read version from __version__.py
def get_version():
    """Get version from __version__.py file"""
    try:
        version_file = Path(__file__).parent / "__version__.py"
        if not version_file.is_file():
            version_file = Path(__file__).parent / NAME / "__version__.py"
        if version_file.is_file():
            with open(version_file, "r") as f:
                for line in f:
                    if line.strip().startswith("version"):
                        parts = line.split("=")
                        if len(parts) == 2:
                            return parts[1].strip().strip('"').strip("'")
    except Exception as e:
        if os.getenv('TRACEBACK') and os.getenv('TRACEBACK') in ['1', 'true', 'True']:
            print(traceback.format_exc())
        else:
            print(f"ERROR: {e}")
    return "3.0.0"


# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name=NAME,
    version=get_version(),
    author="Hadi Cahyadi",
    author_email="cumulus13@gmail.com",
    description="Extended pathlib with 40+ additional utility methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cumulus13/pathlib3",
    project_urls={
        "Bug Tracker": "https://github.com/cumulus13/pathlib3/issues",
        "Documentation": "https://pathlib3.readthedocs.io",
        "Source Code": "https://github.com/cumulus13/pathlib3",
        "Repository": "https://github.com/cumulus13/pathlib3.git",
        "Issues":"https://github.com/cumulus13/pathlib3/issues",
        "Changelog": "https://github.com/cumulus13/pathlib3/blob/main/CHANGELOG.md",
    },
    packages=[NAME],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Filesystems",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.6",
    keywords="pathlib path file filesystem directory utility",
    license="MIT",
    license_files=("LICENSE"),
)
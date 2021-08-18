#!/usr/bin/env python3
from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


setup(
    name="pyopensprinkler",
    version="2.0",
    description="pyopensprinkler",
    author="philmottin",
    author_email="philmottin@philmottin.com",
    url="http://github.com/philmottin/pyopensprinkler",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=True,
    keywords="homeautomation",
)
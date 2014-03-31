#!/usr/bin/env python

from setuptools import setup, find_packages

name = "guesslanguage"

long_description = """
Guess the language of given text.Even works for text containing
multiple languages.

This module is just wrapper against guess-language module of Kent S
Jhonson. It uses langdetect feature from silpa-common module when
guess-language returns UNKNOWN
"""
setup(
    name=name,
    version="0.3",
    url="http://silpa.org.in/Guess_Language",
    license="LGPL-2.1+",
    description="Guess primary language of given text",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools', 'silpa_common', 'guess-language'],
    platforms=['any'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: DFSG approved",
        "License :: OSI Approved :: GNU Lesser General Public License \
        v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
        "Programming Langauge :: Python",
        "Programming Language :: Python :: 2"
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    )

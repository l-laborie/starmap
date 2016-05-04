#!/usr/bin/env python

from setuptools import setup, find_packages

import starmap


NAME = 'starmap'
CLASSIFIERS = [
    "Programming Language :: Python",
    "Development Status :: 1 - Planning",
    "Environment :: Web Environment",
    "Framework :: Django",
    "License :: Apache License 2.0",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Astronomy",
]


setup(
    name=NAME,
    version=starmap.__version__,
    packages=find_packages(),
    author="ludovic laborie",
    description="StarMap is an API to forge sky map to watch sky.",
    long_description=open('README.rst').read(),
    install_requires=open('requirements/base.txt').read(),
    include_package_data=True,
    url='https://github.com/l-laborie/starmap',
    classifiers=CLASSIFIERS,
)

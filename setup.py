#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='k-sequencing',
    version='0.0.6rc',
    description='k-sequencing client for python user',
    url='https://datawow.io',
    author='Datawow.io',
    author_email='info@datawow.io',
    license='MIT',
    packages=['k_sequencing'],
    install_requires=['requests', 'mock >= 2.0.0'],
    test_suite='k_sequencing.test',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ]
)

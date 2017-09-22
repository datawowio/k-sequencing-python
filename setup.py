#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='k-sequencing',
    version='0.0.1rc',
    description='k-sequencing client for python user',
    url='https://datawow.io',
    author='Datawow.io',
    author_email='info@datawow.io',
    license='MIT',
    packages=['k_sequencing'],
    install_requires=['requests'],
    # tests_require=['nose >= 1.3.4', 'mock >= 1.0.1'],
    test_suite='k_sequencing.test'
    # package_data={'sample': ['package_data.dat']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ]
)

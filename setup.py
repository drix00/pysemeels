#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as history_file:
    requirements = history_file.read()

# requirements = [
#     "numpy",
#     "h5py",
# ]

test_requirements = [
    "nose",
]

packages = find_packages()

setup(
    name='pysemeels',
    version='0.1.0',
    description="Python scripts to analyze SEM EELS data",
    long_description=readme + '\n\n' + history,
    author="Hendrix Demers",
    author_email='hendrix.demers@mail.mcgill.ca',
    url='https://github.com/drix00/pysemeels',
    packages=packages,
    package_dir={'pysemeels':
                 'pysemeels'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='pysemeels',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

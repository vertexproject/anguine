#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='anguine',
    version='0.0.0',
    description='anguine',
    author='visi',
    author_email='visi@vertex.link',
    url='https://github.com/vertexproject/anguine',
    license='Apache License 2.0',

    #packages=find_packages(exclude=['*.tests', '*.tests.*']),
    #include_package_data=True,

    install_requires=[
    ],

    classifiers=[
        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: Apache Software License',

        'Topic :: System :: Software Distribution',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

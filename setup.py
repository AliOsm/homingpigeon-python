#! /usr/bin/python

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='HomingPigeon',
    version='1.0',
    author='Ali Fadel',
    author_email='aliosm1997@gmail.com',
    license='MIT',
    description='Homing Pigeon utility package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aliosm/homingpigeon',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

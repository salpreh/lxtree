# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path
import re


# Get current version
version = '1.0.0'
version_input_path = Path('./setup/version.txt')
if version_input_path.exists():
    with open(version_input_path, 'r') as f:
        version_input = f.readline().rstrip()

    if re.match('\\d+\\.\\d+\\.\\d+', version_input):
        version = version_input

# Load doc
with open('README.md') as f:
    readme = f.read()

setup(
    name='lxtree',
    version=version,
    description='Package to draw tree structures (tree linux command style)',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='salpreh',
    author_email='salva.perez46@gmail.com',
    url='https://github.com/salpreh/lxtree',
    license='MIT License',
    packages=find_packages(exclude=('test', 'assets', 'venv', 'doc'))
)

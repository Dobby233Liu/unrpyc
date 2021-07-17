#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name='unrpyc-instructer',
    version='1.2.0',
    description='Tool to decompile Ren\'Py compiled .rpyc script files (instructer fork)',
    long_description=readme(),
    url='https://github.com/Dobby233Liu/unrpyc/tree/dev-instructer',
    packages=['unrpyc', 'unrpyc.decompiler'],
    zip_safe=False,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': ['unrpyc=unrpyc:main'],
    },
)

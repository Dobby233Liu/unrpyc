#!/usr/bin/env python
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name='unrpyc-instructer',
    version='1.0',
    description='Tool to decompile Ren\'Py compiled .rpyc script files (instructer fork)',
    long_description=readme(),
    url='https://github.com/Dobby233Liu/unrpyc/tree/dev-instructer',
    py_modules=['unrpyc'],
    packages=['decompiler'],
    scripts=['unrpyc.py', 'deobfuscate.py'],
    zip_safe=False,
)

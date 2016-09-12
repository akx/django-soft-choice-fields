# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-soft-choice-fields',
    version='0.1.0',
    author='Aarni Koskela',
    author_email='akx@iki.fi',
    packages=find_packages('.', include=('softchoice*')),
    include_package_data=True,
    license='MIT',
)

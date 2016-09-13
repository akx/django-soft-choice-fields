# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='django-soft-choice-fields',
    version='0.3.0',
    author='Aarni Koskela',
    author_email='akx@iki.fi',
    packages=find_packages('.', include=('softchoice*')),
    include_package_data=True,
    license='MIT',
)

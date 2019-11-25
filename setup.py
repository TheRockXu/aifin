#!/usr/bin/env python

from distutils.core import setup

setup(name='aifin',
      version='1.0',
      description='Python Distribution Utilities',
      author='Rocky Xu',
      author_email='percyxu@hotmail.com',
      url='aitroopers.com',
      packages=['aifin'],
            install_requires=[
            'pandas','scipy'
      ]
     )

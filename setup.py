# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='wavebench',
      version='0.1',
      description='wavebench',
      author='Tianlin Liu',
      author_email='t.liu@unibas.ch',
      license='MIT',
      packages=find_packages(include=['wavebench', 'wavebench.*']),
      zip_safe=False)


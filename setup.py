#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name="castest",
      version="1.0",
      description="test logging truncation",
      author="Aaron Daubman",
      package_dir={'': 'castest'},
      packages=['repro_error', 'test_log'],
      install_requires=['cassandra'],
      dependency_links=['https://github.com/datastax/python-driver/archive/master.zip#egg=cassandra']
)


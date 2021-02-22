#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from glob import iglob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


setup(
    name='{{ cookiecutter.plugin_name }}',
    version='{{ cookiecutter.plugin_version}}',
    description='{{ cookiecutter.plugin_description}}',
    author='{{ cookiecutter.plugin_author }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[Path(f).stem for f in iglob('src/*.py')],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'cmd2', 'pluginlib'
    ],
    entry_points = {
        '{{ cookiecutter.plugin_entry_point }}' : [
            'fruits = {{ cookiecutter.plugin_name }}.fruits:LoadableFruits',
            'vegetables = {{ cookiecutter.plugin_name }}.vegetables:LoadableVegetables'
            ],
     '{{ cookiecutter.settable_entry_point }}' : [
            'settables = {{ cookiecutter.plugin_name }}.settables:ProduceSettables',
            ]
        
    },
)

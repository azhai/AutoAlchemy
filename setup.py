#!/usr/bin/env python

from distutils.core import setup
from autoalchemy import __version__

setup(name='AutoAlchemy',
    version=__version__,
    description='AutoAlchemy: Generate models for SQLAlchemy, from the existing tables.',
    author='Ryan Liu',
    author_email='azhai@126.com',
    url='https://github.com/azhai',
    packages=['autoalchemy'],
    install_requires=[
        'SQLAlchemy>=0.7',
        'sqlautocode>=0.7',
        #'Flask>=0.8',
        #'Flask_SQLAlchemy>=0.16',
    ],
    license="BSD",
    platforms=["any"],
)

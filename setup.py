#!/usr/bin/env python

from distutils.core import setup

setup(
        name='django-testshell',
        version='0.1',
        description='Django testshell management command',
        author='Jon Raphaelson',
        author_email='jonraphaelson@gmail.com',
        url='http://www.github.com/lygaret/django-testshell',
        packages=['testshell', 'testshell.management', 'testshell.management.commands']
)

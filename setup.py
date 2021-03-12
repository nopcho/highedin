# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in highedin/__init__.py
from highedin import __version__ as version

setup(
	name='highedin',
	version=version,
<<<<<<< HEAD
	description='highedin',
	author='highedin',
	author_email='highedin',
=======
	description='An information system for management of teaching, research, and academic services in higdepartments or schools of higher education institutes.',
	author='Nopporn Chotikakamthorn',
	author_email='noppcho@gmail.com',
>>>>>>> 04973ea5e9ae9060a2d5f80e3186cb2934d2d23d
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

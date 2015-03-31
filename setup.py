# coding: utf-8
from __future__ import absolute_import

import os

from setuptools import find_packages
from setuptools import setup


#/
setup(
    name='AoikFileTypeAsso',

    version='0.2',

    description="""Creates Windows Registry files (i.e. ".reg" files) to change file type association settings.""",

    url='https://github.com/AoiKuiyuyou/AoikFileTypeAsso',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='windows registry file extension file type association',

    install_requires=[
        'PyYAML',
        #'pywin32', # Not installable via PyPI.
    ],

    package_dir = {'':'src'},

    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoikfiletypeasso=aoikfiletypeasso.main.aoikfiletypeasso:main',
        ],
    },
)

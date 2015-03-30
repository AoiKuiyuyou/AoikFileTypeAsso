import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikWinFileTypeAsso',

    version='0.1.1',

    description="""AoikWinFileTypeAsso is a console program that creates Windows Registry files (i.e. ".reg" files) to change file type association settings.""",

    url='https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso',

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

    keywords='Windows Registry File Extension File Type Association',

    install_requires=[
        'pyyaml',
        #'pywin32',
        ## pywin32 cannot be installed via PyPI so do not list it here.
    ],

    package_dir = {'':'src'},

    packages=find_packages('src', exclude=['contrib', 'docs', 'tests*']),

    package_data={
        'aoikwfta': [
            '*.yaml',
            '*.txt',
        ],
    },

    entry_points={
        'console_scripts': [
            'aoikwfta=aoikwfta.cmd:main',
        ],
    },
)

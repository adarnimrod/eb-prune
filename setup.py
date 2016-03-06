#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='eb-prune',
    version='0.2.0',
    description='Pruning of Elastic Beanstalk versions.',
    long_description=open('README.rst', 'r').read(),
    url='https://www.shore.co.il/cgit/eb-prune',
    author='Nimrod Adar',
    author_email='nimrod@shore.co.il',
    license='MIT',
    classifiers=[
        'Development status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
    ],
    keywords='beanstalk AWS',
    packages=find_packages(),

)

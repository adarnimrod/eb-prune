#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="eb-prune",
    version=open("VERSION", "r").read(),
    description="Pruning of Elastic Beanstalk versions.",
    long_description=open("README.rst", "r").read(),
    url="https://www.shore.co.il/git/eb-prune",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 2",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
    ],
    keywords="beanstalk AWS",
    packages=find_packages(),
    install_requires=["botocore"],
    extras_require={
        "dev": ["pre-commit", "twine"],
    },
    entry_points={
        "console_scripts": ["eb-prune=eb_prune:main"],
    },
)

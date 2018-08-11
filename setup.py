# coding: utf-8
from distutils.core import setup
from setuptools import find_packages


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


requirements = parse_requirements("requirements.txt")

setup(name='soccer_predictions',
      version='1.0',
      description='A simple project for soccer results prediction',
      author='Rémy Frenoy',
      author_email='rfrenoy@gmail.com',
      include_package_data=False,
      install_requires=requirements,
      packages=find_packages(exclude=['tests']),
      long_description=open("README.md").read()
      )

from setuptools import setup
from setuptools import find_packages

setup(
    name='django',
    install_requires=['django'],
    zip_safe=False,
    packages=find_packages(),
)

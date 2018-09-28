from setuptools import setup, find_packages
import os


setup(
    name='testrepo',
    version="0.1",
    zip_safe=False,
    packages=find_packages(),
    author="David E. Koneridng",
    author_email="dek@konerding.com",
    description=("test repo"),
    long_description="Lots of stuff",
    scripts=["main.py"]
)

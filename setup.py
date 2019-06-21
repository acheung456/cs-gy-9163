from distutils.core import setup
from setuptools import find_packages

setup(
    name="crop",
    version="1.0",
    description="Crops images",
    packages=find_packages(),
    install_requires=[
        "Click",
        "click-log",
        "Pillow"
    ],
    entry_points='''
        [console_scripts]
        crop=croptool.cli.crop:cli
    '''
)

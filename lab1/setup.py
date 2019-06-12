from distutils.core import setup

setup(
    name="crop",
    version="1.0",
    description="Crops images",
    packages=["croptool.cli"],
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

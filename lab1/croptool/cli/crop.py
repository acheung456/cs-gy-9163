import click
import click_log
import os

from PIL import Image


@click.group()
def cli():
    """Image Cropper"""
    pass


@cli.command()
@click.option(
    "-s", "--source",
    type=click.Path(exists=True, readable=True)
)
@click.option(
    "-d", "--destination",
    type=click.Path(exists=True, readable=True)
)
def square(source, destination):
    """Square Crop that image"""
    try:
        src = Image.open(source)
    except AttributeError:
        print("Unable to read source image data. Exiting.")
        raise SystemExit
    cropped = src.resize((min(src.size), min(src.size)))
    destination = destination or source
    try:
        cropped.save(destination)
    except IOError:
        print("Unable to save", cropped)

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
    src = Image.open(source)
    cropped = src.crop((0, 0, min(src.size), min(src.size)))
    destination = destination or source
    try:
        cropped.save(destination)
    except IOError:
        print("Unable to save", cropped)

    
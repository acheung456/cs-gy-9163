import click
import click_log
import os
import time
import math

from PIL import Image


@click.group()
def cli():
    """Image Cropper"""
    pass


@cli.command()
@click.option(
    "-s", "--source",
    required=True,
    type=click.Path(exists=True, readable=True),
    help='Source file path'
)
@click.option(
    "-d", "--destination",
    type=click.Path(writable=True),
    help='Destination file path'
)
def square(source, destination):
    """Square crops an image (crops center of image).

    Cropped center image will be transposed up and left
    for half pixel cases.

    :param string source: Source file path
    :param string destination: Destination file path
    """
    
    src = Image.open(source)
    box = (
            0 if min(src.size) == src.size[0] else (src.size[0]-min(src.size))/2,
            0 if min(src.size) == src.size[1] else (src.size[1]-min(src.size))/2,
            min(src.size) if min(src.size) == src.size[0] else src.size[0] - ((src.size[0]-min(src.size))/2),
            min(src.size) if min(src.size) == src.size[1] else src.size[1] - ((src.size[1]-min(src.size))/2)
        )
    box = (math.floor(x) for x in box)
    cropped = src.crop(box)
    destination = destination or source
    try:
        cropped.save(destination)
    except Exception:
        print(f"Unable to save image at {destination}")
        raise

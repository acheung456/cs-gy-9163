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
    type=click.Path(exists=False)
)
def square(source, destination):
    """Square Crop that image"""
    src = Image.open(source)
    box = (
            0 if min(src.size) == src.size[0] else (src.size[0]-min(src.size))/2,
            0 if min(src.size) == src.size[1] else (src.size[1]-min(src.size))/2,  
            min(src.size) if min(src.size) == src.size[0] else src.size[0] - ((src.size[0]-min(src.size))/2),
            min(src.size) if min(src.size) == src.size[1] else src.size[1] - ((src.size[1]-min(src.size))/2)
        )
    cropped = src.crop(box)
    destination = destination or source
    try:
        cropped.save(destination)
    except IOError:
        print("Unable to save", cropped)

    
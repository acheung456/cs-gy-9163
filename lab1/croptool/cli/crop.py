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
    required=True,
    type=click.Path(exists=True, readable=True)
)
@click.option(
    "-d", "--destination",
    type=click.Path(writable=True)
)
def square(source, destination):
    """Square Crop that image"""
    try:
        src = Image.open(source)
    except Exception:
        print(f"Unable to read source image data. Does {source} exist? Is it readable?")
        raise SystemExit
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
        print(f"Unable to save image at {destination}")

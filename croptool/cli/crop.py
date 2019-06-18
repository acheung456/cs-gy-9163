import click
import croptool.crop as crop

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
    crop.square(source, destination)

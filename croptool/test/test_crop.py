import unittest
import os

from croptool.cli import crop
from click.testing import CliRunner
from PIL import Image


class TestCrop(unittest.TestCase):
    def test_crop_with_explicit_destination(self):
        runner = CliRunner()
        raw_image = os.path.join(os.path.dirname(__file__), "../resources/longcrop.png")
        out_image = '/tmp/test_output.png'
        runner.invoke(crop.cli, ['square', '-s', raw_image, '-d', out_image])
        image = Image.open(raw_image)
        new_image = Image.open(out_image)
        x, y = new_image.size[0], new_image.size[1]
        self.assertEqual(min(image.size), x)
        self.assertEqual(min(image.size), y)

    def test_cant_save_new_image(self):
        runner = CliRunner()
        raw_image = os.path.join(os.path.dirname(__file__), "../resources/longcrop.png")
        out_image = '/does/not/exist.png'
        with self.assertRaises(Exception):
            runner.invoke(crop.cli, ['square', '-s', raw_image, '-d', out_image], catch_exceptions=False)

    def test_crop_with_transposed_image(self):
        runner = CliRunner()
        raw_image = os.path.join(os.path.dirname(__file__), "../resources/rectangle.png")
        out_image = '/tmp/test_output.png'
        runner.invoke(crop.cli, ['square', '-s', raw_image, '-d', out_image])
        image = Image.open(raw_image)
        new_image = Image.open(out_image)
        x, y = new_image.size[0], new_image.size[1]
        self.assertEqual(min(image.size), x)
        self.assertEqual(min(image.size), y)

    def test_valid_direction(self):
        from croptool.crop import Directions
        self.assertEqual("up", Directions("up").value)

    def test_invalid_direction(self):
        from croptool.crop import Directions
        self.assertEqual(False, Directions.has_direction("foobar"))

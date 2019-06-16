import unittest
import os

from croptool.cli import crop
from click.testing import CliRunner
from PIL import Image


class TestCrop(unittest.TestCase):
    def test_crop(self):
        runner = CliRunner()
        raw_image = os.path.join(os.path.dirname(__file__), "../resources/longcrop.png")
        out_image = '/tmp/test_output.png'
        result = runner.invoke(crop.cli, ['square', '-s', raw_image, '-d', out_image])
        image = Image.open(raw_image)
        print(result.stdout)
        new_image = Image.open(out_image)
        print(new_image.size)
        x, y = new_image.size[0], new_image.size[1]
        self.assertEqual(min(image.size), x)
        self.assertEqual(min(image.size), y)


if __name__ == '__main__':
    unittest.main()

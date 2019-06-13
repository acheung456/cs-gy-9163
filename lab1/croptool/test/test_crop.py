import unittest
import croptool.cli.crop

from click.testing import CliRunner
from PIL import Image

runner = CliRunner()


class TestCrop(unittest.TestCase):
    def test_crop(self):
        raw_image = "../resources/rectangle.png"
        runner.invoke(croptool.cli.crop.cli(), ['square', '-s', raw_image, '-d', './test_output'])
        image = Image.open(raw_image)

        new_image = Image.open("./test_output")
        self.assertEqual(min(image.size), new_image.size[0])
        self.assertEqual(min(image.size), new_image.size[1])


if __name__ == '__main__':
    unittest.main()

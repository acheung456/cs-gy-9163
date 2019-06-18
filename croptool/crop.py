import math
import PIL

from enum import Enum

def square(source, destination):
    """Square crops an image (crops center of image)"""
    src = PIL.Image.open(source)
    image_box = ImageBox(src.size)
    image_box.center_crop()
    if not all(x % 1 == 0 for x in image_box.box):
        image_box.transpose()
    cropped = src.crop(image_box.box)
    destination = destination or source
    try:
        cropped.save(destination)
    except Exception:
        print(f"Unable to save image at {destination}")
        raise

class Directions(Enum):
    UP = "up"
    DOWN = "down"

    @classmethod
    def has_direction(self, val):
        return any(val == item.value for item in self)

class ImageBox():
    def __init__(self, image_size=(0, 0)):
        self.size = image_size
        self.box = (0, 0) + image_size

    def center_crop(self):
        self.box =  (
            0 if min(self.size) == self.size[0] else (self.size[0]-min(self.size))/2,
            0 if min(self.size) == self.size[1] else (self.size[1]-min(self.size))/2,
            min(self.size) if min(self.size) == self.size[0] else self.size[0] - ((self.size[0]-min(self.size))/2),
            min(self.size) if min(self.size) == self.size[1] else self.size[1] - ((self.size[1]-min(self.size))/2)
        )

    def transpose(self, direction=Directions.UP):
        direction = direction or Directions(direction)
        if direction is Directions.UP:
            self.box = (math.floor(x) for x in self.box)

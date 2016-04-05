__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .. import constants


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def tile(self):
        return self.x // constants.TILE_SIZE, self.y // constants.TILE_SIZE

    @tile.setter
    def tile(self, pos):
        self.x = pos[0] * constants.TILE_SIZE
        self.y = pos[1] * constants.TILE_SIZE
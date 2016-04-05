__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pickle

from ... import debug
from . import blocks


class Layer:
    def __init__(self, content=None):
        self.content = content if content else []

    def get_block_at(self, x, y):
        if 0 <= x < len(self.content[0]) and 0 <= y < len(self.content):
            return self.content[int(y)][int(x)]
        return blocks.block.Block(True)

    def remove_block_at(self, x, y):
        if 0 <= x < len(self.content[0]) and 0 <= y < len(self.content):
            block = self.content[y][x]
            self.content[y][x] = blocks.block.Block(False, False, False)
            return block
        raise ValueError("The block in (x:{}, y:{}) does not exist".format(x, y))

    def set_block_at(self, x, y, block):
        self.content[y][x] = block

    def load(self, path):
        debug.println(path)
        try:
            with open(path, "rb") as file:
                self.content = pickle.Unpickler(file).load()
        except EOFError:
            debug.println("EOFError")
            self.content = []
        except OSError:
            debug.println("OSError")
            self.content = []

    def save(self, path):
        with open(path, "wb") as file:
            pickle.Pickler(file).dump(self.content)
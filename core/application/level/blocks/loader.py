__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame
import os
from glob import glob


class Loader:
    def __init__(self, path_to_sprites):
        self.path_to_sprites = path_to_sprites
        self.sprites = {}
        self._specials_codes = [
            "2000"
        ]

    def load(self):
        for path in glob(os.path.join(self.path_to_sprites, "*.png")):
            code = os.path.split(path)[1].split('.')[0]
            self.sprites[code] = pygame.image.load(path).convert_alpha()
            if code in self._specials_codes:
                self.sprites[code].set_alpha(156)
                self.sprites[code].convert_alpha()
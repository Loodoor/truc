__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame

from . import constants


def println(*args, sep=" ", end="\r\n"):
    if constants.DEBUG_LEVEL == 1:
        print(*args, sep=sep, end=end)


def show_fps(surface, font, fps):
    text = font.render("%3i FPS" % int(fps), 1, constants.WHITE)
    pygame.draw.rect(surface, constants.BLACK, (0, 0, text.get_width() + 4, text.get_height() + 4))
    surface.blit(text, (2, 2))
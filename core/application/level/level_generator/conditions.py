# -*- coding: utf-8 -*-

import random

from . import properties as property
from .blocks import *


def TREE(map_, pos):
    x, y = pos
    if map_[x, y + 1] in (DIRT, GRASS) \
            and map_[x + 1, y + 1] in (DIRT, GRASS) \
            and not map_[x, y] \
            and not map_[x + 1, y]:
        tree = random.randint(0, 1000) in range(property.tree_rate)
        return tree


def HOUSE(map_, pos):
    x, y = pos
    if map_[x - 3, y + 1] \
            and map_[x - 2, y + 1] \
            and map_[x - 1, y + 1] \
            and map_[x, y + 1] \
            and map_[x + 1, y + 1] \
            and map_[x + 2, y + 1] \
            and map_[x + 3, y + 1] \
            and map_[x - 3, y] \
            and not map_[x - 2, y] \
            and not map_[x - 1, y] \
            and not map_[x, y] \
            and not map_[x + 1, y] \
            and not map_[x + 2, y] \
            and not map_[x + 3, y]:
        return random.randint(0, 1000) in range(property.house_rate)
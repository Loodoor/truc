# -*- coding: utf-8 -*-

from random import choice

from .blocks import *
from . import conditions as condition


class Structure:
    structures = []

    def __init__(self, pattern, base, cond=lambda: True):
        self.pattern = pattern
        self.base = base
        self.cond = cond

        Structure.structures.append(self)

    def substitute(self, x, y):
        base_x, base_y = self.base
        get_absolute = lambda rel_x, rel_y: (x + rel_x, y + rel_y)
        get_relative_from_base = lambda abs_x, abs_y: (abs_x - base_x, abs_y - base_y)

        block_dict = {}
        for iy, line in enumerate(self.pattern()):
            for ix, block in enumerate(line):
                if block is not None:
                    block = Block.from_id[block]
                    abs_pos = get_absolute(*get_relative_from_base(ix, iy))
                    block_dict[abs_pos] = block
        return block_dict.items()


TREE = Structure(
    lambda: [
        [None, None, None, 6   , 6   , 6   , 6   , None, None, None],
        [None, 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   ],
        [6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   ],
        [6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   ],
        [6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   , 6   ],
        [None, None, 6   , 6   , 6   , 6   , 6   , 6   , None, None],
        [None, None, None, None, 5   , 5   , 5   , None, None, None],
        [None, None, None, None, 5   , 5   , None, None, None, None],
        [None, None, None, None, 5   , 5   , None, None, None, None],
        [None, None, None, None, 5   , 5   , None, None, None, None],
        [None, None, None, None, 5   , 5   , None, None, None, None]
    ],
    base=(4, 10),
    cond=condition.TREE
)

HOUSE = Structure(
    lambda: [
        [None, None, None, 14  , None, None, None],
        [None, None, 14  , 14  , 14  , None, None],
        [None, 14  , 14  , 7   , 14  , 14  , None],
        [14  , 14  , 7   , 14  , 7   , 14  , 14  ],
        [14  , 7   , 14  , 8   , 14  , 7   , 14  ],
        [14  , 8   , 14  , 8   , 14  , 8   , 14  ],
        [14  , 8   , 14  , 8   , 14  , 8   , 14  ],
        [14  , 7   , 14  , 18  , 14  , 7   , 14  ],
        [14  , 7   , 14  , 18  , 14  , 7   , 14  ],
        [14  , 8   , 0   , 18  , 0   , 8   , 14  ],
        [14  , 7   , 0   , 18  , 0   , 7   , 14  ]
    ],
    base=(3, 10),
    cond=condition.HOUSE
)
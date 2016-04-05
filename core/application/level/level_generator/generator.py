__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .gentest import Map
from ..blocks import block
from .blocks import *
from ..blocks.constants import *


def generate_map(length, flatness, height, headstart, deniv):
    noise = Map(length, flatness, range(1, height), headstart, deniv)
    noise_rework = []
    for line in noise:
        a_line = []
        for case in line:
            a_line.append(
                block.Block(
                    not not case,
                    True,
                    not not case,
                    str(case.ID),
                    TARGET_WOODS if isinstance(case, Wood) else TARGET_STONES if isinstance(case, Mineral) else ALL_TARGETS
                )
            )
        noise_rework.append(a_line)
    return noise_rework
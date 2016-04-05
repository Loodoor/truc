__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


class Block:
    def __init__(self, blocking=False, has_gravity=False, cast_shadow=True, id_="0", kind=None):
        self.blocking = blocking
        self.has_gravity = has_gravity
        self.id = id_
        self.cast_shadow = cast_shadow
        self.kind = kind
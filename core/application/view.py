__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import pygame


class View:
    seed = -1

    def __init__(self, *surfaces):
        self.surfaces = list(surfaces)

    @staticmethod
    def gen_uid() -> int:
        View.seed += 1
        return View.seed

    @staticmethod
    def load(surfaces: list):
        for surface_detail in surfaces:
            try:
                surface_detail['image'] = pygame.image.load(surface_detail['path']).convert_alpha()
            except KeyError:
                if 'surface' in surface_detail.keys() and isinstance(surface_detail['surface'], pygame.Surface):
                    surface_detail['image'] = surface_detail['surface']

            if 'id' not in surface_detail.keys():
                surface_detail['id'] = View.gen_uid()

    def move(self, uid, vector2: pygame.math.Vector2):
        for surface_details in self.surfaces:
            if surface_details['id'] == uid:
                surface_details['position'].x += vector2.x
                surface_details['position'].y += vector2.y

    def add_surf(self, **kwargs):
        pos = kwargs.get('position', kwargs.get('pos', (0, 0)))
        surface = kwargs.get('image', kwargs.get('surface', None))
        seed = kwargs.get('identifier', kwargs.get('id', View.gen_uid()))

        if surface:
            self.surfaces.append(
                {
                    'image': surface,
                    'position': pos,
                    'id': seed
                }
            )
        else:
            raise ValueError("Can not found a valid image / surface")

    def add(self, *surfaces, pos: int=-1):
        View.load(list(surfaces))

        if pos == -1:
            for surf in surfaces:
                self.surfaces.append(surf)
        else:
            self.surfaces[pos:pos] = list(surfaces)

    def draw(self, ecran: pygame.Surface, dt: float):
        for surface_detail in self.surfaces:
            ecran.blit(surface_detail['image'], surface_detail['position'])
__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from . import view
from . import scene_manager
from .. import constants

import pygame
from pygame.locals import *


class App:
    def __init__(self):
        # managers
        self.sc_manager = scene_manager.SceneManager(
            "menu",
            "game"
        )

        # entités

        # constantes
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()

    def load(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.W, constants.H))

        f = pygame.Surface((100, 100))
        f.fill(pygame.Color(180, 20, 20))

        d = pygame.Surface((250, 100))
        d.fill(pygame.Color(20, 180, 20))

        self.sc_manager.associate_view_to_scene(
            "menu",
            view.View(
                {
                    "position": pygame.math.Vector2(0, 0),
                    "surface": f,
                    "id": "rouge"
                },
                {
                    "position": pygame.math.Vector2(50, 50),
                    "surface": d,
                    "id": "vert"
                }
            )
        )

        self.sc_manager.load_scenes_view()

    def render(self, dt: float):
        self.sc_manager.draw_current(self.screen, dt)

    def process_event(self, ev: pygame.event):
        # global
        if ev.type == QUIT:
            self.running = False

        # specific
        if self.sc_manager.current == "menu":
            if ev.type == MOUSEBUTTONUP:
                self.sc_manager.get_view().move("rouge", pygame.math.Vector2(10, 10))

    def run(self):
        self.load()

        while self.running:
            dt = self.clock.tick(constants.FPS) / 1000

            self.process_event(pygame.event.poll())

            self.screen.fill(0)
            self.render(dt)

            pygame.display.flip()
        pygame.quit()
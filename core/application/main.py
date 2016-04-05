__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from . import view
from . import scene_manager
from .. import constants
from .. import debug
from . import level

import os
import pygame
from pygame.locals import *


class App:
    def __init__(self):
        # managers
        self.sc_manager = scene_manager.SceneManager(
            "menu",
            "game"
        )
        self.level = level.level.Level()
        self._blocks_loader = level.blocks.loader.Loader(os.path.join("assets", "blocks"))

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
        self.sc_manager.set_as_dynamic("game")

        self._blocks_loader.load()

        debug.println("Preparing the game")
        pygame.key.set_repeat(200, 100)
        if not os.path.exists("saves/"):
            os.mkdir("saves/")
            debug.println("    Creating map")
            noise = level.level_generator.generator.generate_map(
                constants.MAP_DEFAULT_LENGTH,
                constants.MAP_DEFAULT_FLATNESS,
                constants.MAP_DEFAULT_HEIGHT,
                constants.MAP_DEFAULT_HEAD_START,
                constants.MAP_DEFAULT_DENIV
            )
            debug.println("    Map created")
            self.level.add_layer(level.layer.Layer(noise))
            self.level.add_layer(level.layer.Layer(noise))
            debug.println("    Layers created and assigned to the level")
        else:
            debug.println("A save was found")
            debug.println("Loading the map")
            self.level.load("saves/world1")
            debug.println("Map loaded")

    def save(self):
        debug.println("Saving world")
        self.level.save("saves/world1")
        debug.println("World saved")
        pygame.quit()

    def render(self, dt: float):
        if not self.sc_manager.is_view_dynamic():
            self.sc_manager.draw_current(self.screen, dt)
        else:
            if self.sc_manager.current == "game":
                for il, layer in enumerate(self.level.layers[::-1]):
                    tmp_layer = [line[self.level.fov[0]:self.level.fov[1]] for line in layer.content][self.level.fov[2]:self.level.fov[3]]
                    for iy, line in enumerate(tmp_layer):
                        for ix, case in enumerate(line):
                            self.sc_manager.get_view().add_surf(
                                image=self._blocks_loader.sprites[case.id],
                                pos=(ix * constants.TILE_SIZE, iy * constants.TILE_SIZE)
                            )

    def process_event(self, ev: pygame.event):
        # global
        if ev.type == QUIT:
            self.running = False

        # specific
        if self.sc_manager.current == "menu":
            if ev.type == MOUSEBUTTONUP:
                self.sc_manager.get_view().move("rouge", pygame.math.Vector2(10, 10))
            if ev.type == KEYUP:
                if ev.key == "j":
                    self.sc_manager.change_current_for("game")
                    debug.println("Entering play mode")

    def run(self):
        self.load()

        while self.running:
            dt = self.clock.tick(constants.FPS) / 1000

            self.process_event(pygame.event.poll())

            self.screen.fill(0)
            self.render(dt)

            pygame.display.flip()

        self.save()
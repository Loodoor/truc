__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from .view import View

import pygame


class SceneManager:
    def __init__(self, *args):
        self.__availables_scenes = args
        self.__dynamics = []
        self.__scenes = {
            scene: None for scene in self.__availables_scenes
        }
        self.current = self.__availables_scenes[0]
        self.__historique = []

    def set_as_dynamic(self, scene: str):
        self.__dynamics.append(scene)

    def is_view_dynamic(self):
        if self.current in self.__dynamics:
            return True
        return False

    def load_scenes_view(self):
        for scene in self.__scenes.values():
            try:
                View.load(scene.surfaces)
            except AttributeError:
                pass

    def get_view(self):
        return self.__scenes[self.current]

    def associate_view_to_scene(self, scene: str, view: View) -> object:
        self.__scenes[scene] = view
        return self

    def draw_current(self, ecran: pygame.Surface, dt: float):
        try:
            self.__scenes[self.current].draw(ecran, dt)
        except AttributeError:
            pass

    def change_current_for(self, new: str):
        self.__historique.append(self.current)
        self.current = new

    def change_for_last(self):
        self.current = self.__historique.pop()
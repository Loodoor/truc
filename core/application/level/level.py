__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

import os
import pickle
import pygame

from . import layer as llayer
from ... import debug
from ...constants import *


class Level:
    def __init__(self):
        self.layers = []
        self._path_to_layers = []
        self.fov = [0, W // TILE_SIZE, 0, H // TILE_SIZE]

    def get_fov(self):
        return self.fov

    def collide_at(self, x, y):
        return self.layers[0].get_block_at(x, y).blocking

    def get_id_at(self, x, y, layer=0):
        return self.layers[layer].get_block_at(x, y).id

    def get_kind_at(self, x, y, layer=0):
        return self.layers[layer].get_block_at(x, y).kind

    def remove_block_at(self, x, y, layer=0):
        return self.layers[layer].remove_block_at(x, y)

    def load(self, path):
        if os.path.exists(os.path.join(path, "level")):
            try:
                with open(os.path.join(path, "level"), "rb") as file:
                    self._path_to_layers = pickle.Unpickler(file).load()
            except EOFError:
                self._path_to_layers = []

            debug.println("Layers list loaded")

        self.load_layers(path)

    def load_layers(self, path):
        debug.println("Loading the layers")
        for path_to_layers in self._path_to_layers:
            layer = llayer.Layer()
            layer.load(os.path.join(path, path_to_layers))
            debug.println("Layer is not empty : {}".format(len(layer.content) > 0))
            self.add_layer(layer)
        debug.println("Layers loaded")

    def save(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        for i, layer in enumerate(self.layers):
            layer.save(os.path.join(path, str(i) + ".layer"))
        with open(os.path.join(path, "level"), "wb") as file:
            pickle.Pickler(file).dump([str(i) + ".layer" for i in range(len(self.layers))])

    def add_layer(self, layer):
        self.layers.append(layer)

    def draw(self, surf: pygame.Surface):
        return surf
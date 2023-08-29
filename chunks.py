from settings import *
import pygame as pg
from blocks import *


class Chunk(pg.sprite.Group):
    def __init__(self, game, x, y, n):
        super(Chunk, self).__init__()
        self.n = n
        self.game = game
        for i in range(CHUNK_SIDE):
            for j in range(CHUNK_SIDE):
                py = (i + y) / WORLD_LENGTH
                px = (j + x) / WORLD_WIDTH
                # print(noise([px, py]), 'noise')
                zz = round_for_n(MIN_GROUND_HEIGHT + (noise([px, py])) * SIDE_SHIFT)
                gr = Grass(self.game, (j + x) * SIDE_SHIFT, (i + y) * SIDE_SHIFT, zz)
                self.add(gr)

    def change_coords(self, dx, dy, dz):
        for block in self.sprites():
            block.change_coords(dx, dy, dz)

    def rotate_cam(self, dir):
        pass

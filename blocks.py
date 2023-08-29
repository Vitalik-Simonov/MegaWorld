import pygame as pg
from settings import *
from math import ceil


class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y, z, im_path):
        super(Block, self).__init__(game.blocks)
        self.x = ceil(x)
        self.y = ceil(y)
        self.z = ceil(z)
        # print(self.x, self.y, self.z)
        # if self.x == self.y == 225:
        #     self.image = pg.image.load('imgs/yellow.png')
        # else:
        self.image = pg.image.load(im_path)
        self.rect = self.image.get_rect()
        self.rect.centerx = cos30 * x - cos30 * y + CAMERA_X
        self.rect.centery = cos60 * x + cos60 * y - z + CAMERA_Y
        self.game = game

    def update(self):
        # print(self.rect.center)
        pass

    def change_coords(self, dx, dy, dz):
        # if dx < 0 or dy < 0:
        #     ddx = cos30 * dy - cos30 * dx
        #     ddy = cos60 * dy + cos60 * dx - dz
        #     self.rect.x += ddx
        #     self.rect.y += ddy
        #     return
        ddx = cos30 * dy - cos30 * dx
        ddy = cos60 * dy + cos60 * dx - dz
        self.rect.x += ddx
        self.rect.y += ddy


class Grass(Block):
    def __init__(self, game, x, y, z):
        super(Grass, self).__init__(game, x, y, z, r'imgs\grass.png')

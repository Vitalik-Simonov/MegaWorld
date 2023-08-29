# 25 - сторона
import pygame as pg
from settings import *
from blocks import *
from chunks import *
import os
import sys
os.chdir('\\'.join(sys.argv[0].split('\\')[:-1]))


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

    def setup(self):
        self.is_game = True
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.chunks = []
        for i in range(0, CHUNK_SIDE * 3 + 1, CHUNK_SIDE):
            for j in range(0, CHUNK_SIDE * 3 + 1, CHUNK_SIDE):
                self.chunks.append(Chunk(self, j, i, j + i))

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    for chunk in self.chunks:
                        chunk.rotate_cam(1)
                if event.key == pg.K_RIGHT:
                    for chunk in self.chunks:
                        chunk.rotate_cam(-1)
        self.all_sprites.update()
        for chunk in self.chunks:
            chunk.change_coords(0, 0, 0)
        for chunk in self.chunks:
            chunk.update()

    def draw(self):
        self.screen.fill('black')
        self.all_sprites.draw(self.screen)
        for chunk in self.chunks:
            chunk.draw(self.screen)
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(str(self.clock.get_fps()))

    def run(self):
        self.setup()
        while self.is_game:
            self.update()
            self.draw()


if __name__ == '__main__':
    app = Game()
    app.run()

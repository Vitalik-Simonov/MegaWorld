from perlin_noise import PerlinNoise


noise = PerlinNoise(octaves=30, seed=10000)
WIDTH = 860 # 1100
HEIGHT = 700
SIDE = 25
SIDE_SHIFT = 24.9
CAMERA_X = WIDTH // 2
CAMERA_Y = HEIGHT // 4
FPS = 45
cos30 = 0.8660254037844387
cos60 = 0.51
WORLD_WIDTH = 500
WORLD_LENGTH = 500
CHUNK_SIDE = 5
MIN_GROUND_HEIGHT = 100

data_is_free = {}


def round_for_n(n, round_for=SIDE):
    return n // round_for * round_for

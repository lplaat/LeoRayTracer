import pygame

def start():
    pygame.init()
    pygame.display.set_caption("RayCaster")

    canvas = pygame.display.set_mode((896, 448), 0, 32)

    map = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]

    keys = [False, False, False, False]
    cell_size = 64

    player = {
        'res': 16,
        'fov': 60,
        'x': 100,
        'y': 100,
        'angle': 0,
        'size': 10,
        'speed': 0
    }

    return (canvas, map, cell_size, keys, player)
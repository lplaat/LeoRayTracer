import pygame, raycaster

def map(canvas, cell_size, map):
    for yt in range(len(map)):
        for xt in range(len(map[yt])):
            if map[yt][xt] == 1:
                pygame.draw.rect(canvas, (0, 0, 255), pygame.Rect(xt * cell_size, yt * cell_size, cell_size, cell_size))

def player(canvas, player):
    pygame.draw.rect(canvas, (0, 255, 0), pygame.Rect(player['x'], player['y'], player['size'], player['size']))
    pygame.draw.line(canvas, (255, 255, 0), (player['x'] + player['size'] / 2, player['y'] + player['size'] / 2), (player['x'] + player['size'] / 2 + raycaster.move_angle(player['angle'], 10)[0], player['y'] + player['size'] / 2 + raycaster.move_angle(player['angle'], 10)[1]), 1)

import pygame
import setup, movement, raycaster, render

canvas, map, cell_size, keys, player = setup.start()

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        movement.update_keys(event, keys)

    player = movement.update(player, cell_size, map)
    raycaster.RayCaster(canvas, player, cell_size, map)

    render.map(canvas, cell_size, map)
    render.player(canvas, player)


    pygame.display.update()
    clock.tick(30)
    canvas.fill((0,0,0))

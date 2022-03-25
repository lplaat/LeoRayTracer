import pygame
import setup, movement, raycaster, render

#setting up game
canvas, map, cell_size, keys, player = setup.start()
exit = False
clock = pygame.time.Clock()

#frame loop
while not exit:
    for event in pygame.event.get():
        #when window is closed
        if event.type == pygame.QUIT:
            exit = True

        #update keys inputs
        movement.update_keys(event, keys)

    #update player movement
    player = movement.update(player, cell_size, map)

    #update raycaster
    raycaster.RayCaster(canvas, player, cell_size, map)

    #render map
    render.map(canvas, cell_size, map)
    render.player(canvas, player)

    #updates the frame
    pygame.display.update()
    clock.tick(30)
    canvas.fill((0,0,0))

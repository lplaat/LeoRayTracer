import pygame, collision, raycaster

#key list
inner_keys = [False, False, False, False]

#set key list to True or False
def key(keys, key_id):
    if keys[key_id] == False:
        keys[key_id] = True
        inner_keys[key_id] = True
    else:
        keys[key_id] = False
        inner_keys[key_id] = False
    return keys

#tries to move player
def TryMove(player, cell_size, map, dx, dy):
    player['x'] += dx
    player['y'] += dy
    if collision.TouchingWall(player, cell_size, map):
        player['x'] += 0 - dx
        player['y'] += 0 - dy

    return player

#update key list when button is pressed
def update_keys(event, keys):
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            keys = key(keys, 0)
        elif event.key == pygame.K_LEFT:
            keys = key(keys, 1)
        elif event.key == pygame.K_RIGHT:
            keys = key(keys, 2)
        elif event.key == pygame.K_DOWN:
            keys = key(keys, 3)

#update player movement
def update(player, cell_size, map):
    player = TryMove(player, cell_size, map, raycaster.move_angle(player['angle'], player['speed'])[0], 0)
    player = TryMove(player, cell_size, map, 0, raycaster.move_angle(player['angle'], player['speed'])[1])

    if inner_keys[0]:
        player['speed'] = 2
    elif inner_keys[3]:
        player['speed'] = -2
    else:
        player['speed'] = 0
    
    if inner_keys[1]:
        player['angle'] -= 0.05
    if inner_keys[2]:
        player['angle'] += 0.05

    return player
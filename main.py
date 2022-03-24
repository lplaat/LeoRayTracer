import pygame, math

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

def move_angle(angle, amount):
    return [math.cos(angle) * amount, math.sin(angle) * amount]

def key(key_id):
    if keys[key_id] == False:
        keys[key_id] = True
    else:
        keys[key_id] = False

def TouchingWall(object, dist_from_wall = False):
    touching = False
    closed_wall = math.inf
    for yt in range(len(map)):
        for xt in range(len(map[yt])):
            dist = math.hypot(object['x'] - xt * cell_size, object['y'] - yt * cell_size)
            if dist < cell_size * 2:
                if dist_from_wall:
                    if closed_wall > dist and dist < cell_size * 1.5:
                        closed_wall = dist

                if map[yt][xt] == 1 and object['x'] > xt*cell_size and object['x'] < xt*cell_size + cell_size:
                    if map[yt][xt] == 1 and object['y'] > yt*cell_size and object['y'] < yt*cell_size + cell_size:
                        touching = True

                if map[yt][xt] == 1 and object['x'] + object['size'] - 1 > xt*cell_size and object['x'] + object['size'] - 1 < xt*cell_size + cell_size:
                    if map[yt][xt] == 1 and object['y'] + object['size'] - 1 > yt*cell_size and object['y'] + object['size'] - 1 < yt*cell_size + cell_size:
                        touching = True

                if map[yt][xt] == 1 and object['x'] + object['size'] - 1 > xt*cell_size and object['x'] + object['size'] - 1 < xt*cell_size + cell_size:
                    if map[yt][xt] == 1 and object['y'] > yt*cell_size and object['y'] < yt*cell_size + cell_size:
                        touching = True

                if map[yt][xt] == 1 and object['x'] > xt*cell_size and object['x'] < xt*cell_size + cell_size:
                    if map[yt][xt] == 1 and object['y'] + object['size'] - 1 > yt*cell_size and object['y'] + object['size'] - 1 < yt*cell_size + cell_size:
                        touching = True

    if dist_from_wall:
        return [touching, closed_wall]
    else:
        return touching

def RayCaster():
    x = 0
    ray_angle = player['angle'] - (player['fov'] / 100) / 2
    scan_lines = 448 / player['res']
    for _ in range(math.floor(scan_lines)):
        distance = Ray(ray_angle)

        if distance == 0:
            distance = 1
        
        height = 8000 / distance

        color = 255 / distance * 100
        if color > 255:
            color = 255
        elif color < 0:
            color = 0

        pygame.draw.rect(canvas, (0, 0, color), pygame.Rect(448 + x, 250-height, player['res'], height*2))

        x += player['res']
        ray_angle += (player['fov'] / scan_lines) / 100

def Ray(angle):
    found = True
    rx = player['x'] + player['size'] / 2
    ry = player['y'] + player['size'] / 2

    dist_from_wall = math.inf
    dist = 0
    while found:
        if dist_from_wall == math.inf:
            steps = 5
        else:
            steps = 2.5

        rx += math.cos(angle) * steps
        ry += math.sin(angle) * steps
        dist += steps

        out = TouchingWall({'x': rx, 'y': ry, 'size': 1}, dist_from_wall = True)
        dist_from_wall = out[1]
        if out[0]:
            found = False

    found = True
    while found:
        rx -= math.cos(angle) * 0.5
        ry -= math.sin(angle) * 0.5
        dist -= 0.5
        if not TouchingWall({'x': rx, 'y': ry, 'size': 1}):
            found = False

    dist = dist * math.cos(player['angle'] - angle)
    return dist - 5

def MovePlayer():
    TryMove(move_angle(player['angle'], player['speed'])[0], 0)
    TryMove(0, move_angle(player['angle'], player['speed'])[1])

def TryMove(dx, dy):
    player['x'] += dx
    player['y'] += dy
    if TouchingWall(player):
        player['x'] += 0 - dx
        player['y'] += 0 - dy

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key(0)
            elif event.key == pygame.K_LEFT:
                key(1)
            elif event.key == pygame.K_RIGHT:
                key(2)
            elif event.key == pygame.K_DOWN:
                key(3)

    if keys[0]:
        player['speed'] = 2
    elif keys[3]:
        player['speed'] = -2
    else:
        player['speed'] = 0
    
    if keys[1]:
        player['angle'] -= 0.05
    if keys[2]:
        player['angle'] += 0.05
    MovePlayer()

    for yt in range(len(map)):
        for xt in range(len(map[yt])):
            if map[yt][xt] == 1:
                pygame.draw.rect(canvas, (0, 0, 255), pygame.Rect(xt * cell_size, yt * cell_size, cell_size, cell_size))

    pygame.draw.rect(canvas, (0, 255, 0), pygame.Rect(player['x'], player['y'], player['size'], player['size']))
    pygame.draw.line(canvas, (255, 255, 0), (player['x'] + player['size'] / 2, player['y'] + player['size'] / 2), (player['x'] + player['size'] / 2 + move_angle(player['angle'], 10)[0], player['y'] + player['size'] / 2 + move_angle(player['angle'], 10)[1]), 1)

    RayCaster()

    pygame.display.update()
    clock.tick(30)
    canvas.fill((0,0,0))

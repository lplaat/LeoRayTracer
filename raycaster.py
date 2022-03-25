import pygame, math, collision

#calculate angle
def move_angle(angle, amount):
    return (math.cos(angle) * amount, math.sin(angle) * amount)

#spawns rays to see the distance off a object
def RayCaster(canvas, player, cell_size, map):
    x = 0
    ray_angle = player['angle'] - (player['fov'] / 100) / 2
    scan_lines = 448 / player['res']
    for _ in range(math.floor(scan_lines)):
        distance = Ray(ray_angle, player, cell_size, map)

        if distance == 0:
            distance = 1
        
        height = 8000 / distance

        color = 255 / distance * 100
        if color > 255:
            color = 255
        elif color < 0:
            color = 0

        pygame.draw.rect(canvas, (0, 0, color), pygame.Rect(448 + x, 224-height, player['res'], height*2))

        x += player['res']
        ray_angle += (player['fov'] / scan_lines) / 100

#calculate distance off how far the wall is with angle
def Ray(angle, player, cell_size, map):
    found = True
    rx = player['x'] + player['size'] / 2
    ry = player['y'] + player['size'] / 2

    dist_from_wall = math.inf
    dist = 0
    while found:
        if dist_from_wall == math.inf:
            steps = 10
        else:
            steps = 1

        rx += math.cos(angle) * steps
        ry += math.sin(angle) * steps
        dist += steps

        out = collision.TouchingWall({'x': rx, 'y': ry, 'size': 1}, cell_size, map, dist_from_wall = True)
        dist_from_wall = out[1]
        if out[0]:
            found = False

    found = True
    while found:
        rx -= math.cos(angle) * 0.5
        ry -= math.sin(angle) * 0.5
        dist -= 0.5
        if not collision.TouchingWall({'x': rx, 'y': ry, 'size': 1}, cell_size, map):
            found = False

    dist = dist * math.cos(player['angle'] - angle)
    return dist - 5
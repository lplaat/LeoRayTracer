import math

#checks when object is in side a wall
def TouchingWall(object, cell_size, map, dist_from_wall = False):
    touching = False
    closed_wall = math.inf
    for yt in range(len(map)):
        for xt in range(len(map[yt])):
            dist = math.hypot(object['x'] - xt * cell_size, object['y'] - yt * cell_size)
            if dist < cell_size * 2:
                if dist_from_wall:
                    if closed_wall > dist and dist < cell_size / 4:
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
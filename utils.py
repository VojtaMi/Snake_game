def check_proximity(pos1, pos2):
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    return dist_x < 1 and dist_y < 1

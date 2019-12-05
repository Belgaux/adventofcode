
def mdist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def intersection(line1, line2):
    """Return point (x, y) where line1 and line2 segments intersect, None if no intersection point.
    http://www.cs.swan.ac.uk/~cssimon/line_intersection.html"""
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    # skip parallel line segments (det == 0)
    if (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) == 0:
        return None

    t = ((x1-x3)*(y3-y4) + (y1-y3)*(x4-x3)) / ((x4-x3)*(y1-y2) - (x1-x2)*(y4-y3))
    u = ((y1-y2)*(x1-x3) + (x2-x1)*(y1-y3)) / ((x4-x3)*(y1-y2) - (x1-x2)*(y4-y3))

    # intersection point
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t*(x2-x1), y1 + t*(y2-y1))
        #return (x3 + u*(x4-x3), y3 + u*(y4-y3))
    else:
        return None

def get_lines(wire):
    lines = []
    cur = [0, 0]
    for w in wire:
        direction = w[0]
        dist = int(w[1:])
        if direction == "U":
            lines.append((cur[0], cur[1], cur[0], cur[1] + dist))
            cur[1] += dist
        elif direction == "D":
            lines.append((cur[0], cur[1], cur[0], cur[1] - dist))
            cur[1] -= dist
        elif direction == "R":
            lines.append((cur[0], cur[1], cur[0] + dist, cur[1]))
            cur[0] += dist
        elif direction == "L":
            lines.append((cur[0], cur[1], cur[0] - dist, cur[1]))
            cur[0] -= dist
    return lines

with open("../inputs/03.txt") as f:
    p = [line.strip() for line in f.readlines()]
    wire1 = p[0].split(",")
    wire2 = p[1].split(",")
    lines1 = get_lines(wire1)
    lines2 = get_lines(wire2)

    # find all intersection points
    ips = [intersection(l1, l2) for l1 in lines1 for l2 in lines2 if intersection(l1, l2)]

    # find intersection point closest to origo
    print(min(mdist((0,0), p) for p in ips if mdist((0,0), p) > 0))


import sys

with open("../inputs/01.txt") as fp:
    instructions = [char.strip() for char in fp.read().split(",")]

distance = lambda x: abs(x[0]) + abs(x[1])
dirs = ("n", "e", "s", "w") # north, east, south, west
i = 0
pos = [0, 0]
visited = []
visited.append(tuple(pos))

# Part 2
def step(coord, dist, negative=False):
    for _ in range(dist):
        if negative:
            pos[coord] -= 1
        else:
            pos[coord] += 1
        if tuple(pos) in visited:
            print("intersection: {} blocks away.".format(distance(pos)))
            sys.exit()
        visited.append(tuple(pos))

for inst in instructions:
    prev = pos
    if inst[0] is "R":
        i += 1
    else:
        i -= 1
    facing = dirs[i % 4]
    dist = int(inst[1:])
    if facing is "n":
        step(1, dist)
    elif facing is "s":
        step(1, dist, negative=True)
    elif facing is "e":
        step(0, dist)
    elif facing is "w":
        step(0, dist, negative=True)

# Part 1
print(distance(pos))

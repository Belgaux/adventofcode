# each cell will contain a list of id's that have a claim there
grid = [[[] for i in range(1000)] for j in range(1000)]
grid_meta = {}

with open("../inputs/03.txt") as f:
    claims = [line.strip() for line in f.readlines()]
    for c in claims:
        # extracting data like this because i hate regex
        _id, rest = c.split("@")
        start_pos, size = rest.split(":")
        start_pos, size = start_pos.strip(), size.strip()
        x, y = start_pos.split(",")
        w, h = size.split("x")
        x, y, w, h = int(x), int(y), int(w), int(h)
        grid_meta[_id] = [x, y, w, h]

        # overlapping squares will create a list on with len(list) > 1
        for i in range(y-1, y-1 + h):
            for j in range(x-1, x-1 + w):
                grid[i][j].append(_id)

# how many cells with more than one claim?
print(len(list(filter(lambda x: len(x) > 1, (cell for row in grid for cell in row)))))

# check which claim has no overlap
for key, value in grid_meta.items():
    x, y, w, h = value
    overlap = 0
    for i in range(y-1, y-1 + h):
        for j in range(x-1, x-1 + w):
            if len(grid[i][j]) > 1:
                overlap += 1
    if overlap == 0:
        print("no overlap:", key, value)


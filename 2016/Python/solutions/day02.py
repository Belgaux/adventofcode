keypad = [[1,2,3],[4,5,6],[7,8,9]]
pos = [1,1]

for line in open("../inputs/02.txt").readlines():
    for char in line:
        if char is "U":
            if pos[0] - 1 >= 0:
                pos[0] -= 1
        elif char is "D":
            if pos[0] + 1 <= 2:
                pos[0] += 1
        elif char is "R":
            if pos[1] + 1 <= 2:
                pos[1] += 1
        elif char is "L":
            if pos[1] - 1 >= 0:
                pos[1] -= 1
    print(keypad[pos[0]][pos[1]], end="")

# part 2
print()

keypad = [[0,  0,   1,   0,  0],
          [0,  2,   3,   4,  0],
          [5,  6,   7,   8,  9],
          [0, "A", "B", "C", 0],
          [0,  0,  "D",  0,  0]]
pos = [2, 0]

for line in open("../inputs/02.txt").readlines():
    for char in line:
        r, c = pos[0], pos[1]
        try:
            if char is "U":
                if keypad[r-1][c] != 0:
                    pos[0] -= 1
            elif char is "D":
                if keypad[r+1][c] != 0:
                    pos[0] += 1
            elif char is "R":
                if keypad[r][c+1] != 0:
                    pos[1] += 1
            elif char is "L":
                if keypad[r][c-1] != 0:
                    pos[1] -= 1
        except:
            # index error, edge
            continue
    print(keypad[pos[0]][pos[1]], end="")


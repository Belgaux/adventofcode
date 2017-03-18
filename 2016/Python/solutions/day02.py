
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

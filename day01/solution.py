with open("input.txt") as f:
    floor = 0
    for char in f.read():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

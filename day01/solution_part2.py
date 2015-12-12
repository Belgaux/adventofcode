with open("input.txt") as f:
    floor = 0;
    for i, char in enumerate(f.read()):
        if floor == -1:
            print("First floor -1 index: ", i)
            break
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

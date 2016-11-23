class Santa():
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.pos = (self.x_pos, self.y_pos)

    def set_pos(self):
        self.pos = (self.x_pos, self.y_pos)

    def move(self, direction):
        if direction == '^':
            self.y_pos += 1
        elif direction == 'v':
            self.y_pos -= 1
        elif direction == '<':
            self.x_pos -= 1
        elif direction == '>':
            self.x_pos += 1
        self.set_pos()

def main():
    # part 1
    houses = {}
    santa = Santa()
    with open("../inputs/input3.txt") as in_file:
        for dest in in_file.read().strip('\n'):
            santa.move(dest)
            houses[santa.pos] = True
    print("houses with at least 1 present: ", len(houses))

    # part 2
    houses = {}
    santa = Santa()
    robot = Santa()

    stack = []
    with open("../inputs/input3.txt") as in_file:
        for dest in in_file.read().strip('\n'):
            stack.append(dest)
    stack.reverse()
    while stack:
        if stack:
            santa.move(stack.pop())
            houses[santa.pos] = True
        if stack:
            robot.move(stack.pop())
            houses[robot.pos] = True
    print("houses with at least 1 present: ", len(houses))

if __name__ == "__main__":
    main()

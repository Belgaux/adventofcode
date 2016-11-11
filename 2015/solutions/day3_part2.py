class Santa():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        self.pos = (self.x, self.y)

def main():
    houses = {}
    santa = Santa()
    robot = Santa()

    stack = []
    with open("../inputs/input3.txt") as f:
        for d in f.read().strip('\n'):
            stack.append(d)
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

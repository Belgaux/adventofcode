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
    with open("../inputs/input3.txt") as f:
        for d in f.read().strip('\n'):
            santa.move(d)
            houses[santa.pos] = True
    print("houses with at least 1 present: ", len(houses))

if __name__ == "__main__":
    main()

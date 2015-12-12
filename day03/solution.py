
class Santa():
    def __init__(self, x=0, y=0):
        self.house_coords = {(x, y): 1} # starting position
        self.x = x
        self.y = y
        
    def move(self, direction):
        if direction == '^':
            self.y -= 1
        elif direction == 'v':
            self.y += 1
        elif direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1

    def deliver_present(self):
        loc = (self.x, self.y)
        if loc in self.house_coords:
            self.house_coords[loc] += 1
        else:
            self.house_coords[loc] = 1

def main():
    s = Santa()
    with open("input.txt") as f:
        for d in f.read():
            s.move(d)
            s.deliver_present()

    at_least_one = 0
    for i in s.house_coords:
        if s.house_coords[i] >= 1:
            at_least_one += 1
    print("Houses receiving at least one present: ", at_least_one)

if __name__ == "__main__":
    main()

with open("input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line.split(" "))

class ALU():
    def __init__(self, operator):
        self.operator = operator

inputs = []
with open("input.txt") as f:
    inputs = f.read().splitlines()

class Wire():
    def __init__(self, input, output):
        self.input = input
        self.output = output

class ControlUnit():
    def __init__(self):

class ALU():

    operators = ("AND", "OR", "NOT", "LSHIFT", "RSHIFT")

    def __init__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

    def decode_instruction(self, args):
        print(args)

    def left_shift(self, op1, op2):
        return op1 << op2

class Circuit():
    def __init__(self):
        self.wires = {}


def main():
    a = ALU()
    print(inputs[1])
    a.decode_instruction(["123", "->", "x"])
    print(a.left_shift())

if __name__ == '__main__':
    main()

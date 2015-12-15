ASSIGNMENT = '->'

def parse_instruction(inst):
    operand_one = None
    operand_two = None
    operator = None
    output = None
    print(inst.split(" "))
    params = inst.split(" ")

    if params[1] == ASSIGNMENT:
        operand_one = params[0]
        operand_two = params[2]
        # assign operand_one -> operand_two
        wires[operand_two] = operand_one
    elif params[0] == 'NOT':
        operator = 'NOT'
        operand_one = params[1]
        output = params[3]
        wires[output] = ALU(op1=operand_one, operator=operator)
    elif params[3] == ASSIGNMENT:
        operand_one = params[0]
        operator    = params[1]
        operand_two = params[2]
        output      = params[4]
    print(operand_one, operand_two, operator, output)

def ALU(op1=None, op2=None, operator=None):
    if operator == 'AND':
        return int(op1 & op2)
    elif operator == 'OR':
        return int(op1 | op2)
    elif operator == 'LSHIFT':
        return int(op1 << op2)
    elif operator == 'RSHIFT':
        return int(op1 >> op2)
    else:
        return ~op1


wires = {}
inputs = []

with open("input.txt") as f:
    inputs = f.read().splitlines()

for line in inputs:
    parse_instruction(line)

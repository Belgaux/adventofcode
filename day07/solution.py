
with open("input.txt") as f:
    inputs = f.read().splitlines()

for line in inputs:
    parse_instruction(line)

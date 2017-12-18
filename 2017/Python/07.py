
def parse(line):
  elems = line.split()
  name = elems[0]
  weight = elems[1][1:-1]
  if len(elems) > 2:
    children = ("".join(elems[3:])).split(",")
    return name, weight, children
  else:
    return name, weight, None

with open("../inputs/07.txt") as f:
  puzzle_input = list(e.strip() for e in f.readlines())
  parent_of = dict()
  nodes = dict()
  for line in puzzle_input:
    name, weight, children = parse(line)
    nodes[name] = weight
    if children:
      for child in children:
        parent_of[child] = name
  print(list(node for node in nodes if node not in parent_of.keys()))


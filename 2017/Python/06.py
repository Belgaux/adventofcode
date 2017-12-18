import itertools

def redistribute(mem):
  banks = {i: e for i, e in enumerate(mem)}
  sorted_by_value = sorted(banks.items(), key=lambda t: (t[1], t[0]))
  chosen = sorted(
      filter(lambda t: t[1] == sorted_by_value[-1][1], sorted_by_value),
      key=lambda t: (t[0], t[1]))[0]
  start, blocks = chosen
  new_mem = list(e for e in mem)
  new_mem[start] = 0
  i = 0
  while blocks > 0:
    new_mem[(start+i+1) % len(new_mem)] += 1
    blocks -= 1
    i += 1
  return tuple(new_mem) # hashable type


with open("../inputs/06.txt") as f:
  mem = tuple(int(e) for e in f.read().split("\t"))
  seen = dict()
  for i in itertools.count(1):
    print(mem)
    mem = redistribute(mem)
    if mem in seen:
      print("Redistributions before finding infinite loop=", i)
      print("Cycles in infinite loop=", i - seen[mem])
      break
    else:
      seen[mem] = i


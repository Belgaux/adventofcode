def escape(maze):
  steps_taken = 0
  sp = 0
  while 0 <= sp < len(maze):
    offset = maze[sp]
    if offset >= 3:
      maze[sp] -= 1
    else:
      maze[sp] += 1
    sp += offset
    steps_taken += 1
  return steps_taken

with open("../inputs/05.txt") as f:
  print(escape(list(int(n) for n in f)))


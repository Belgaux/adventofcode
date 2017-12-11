
def step_length(move, k):
  """
  Number of times to move in a direction.
  k is the block index, a block is R* U* L* D*
  """ 
  moves = {"R": 2*k+1, "U": 2*k+1, "L": 2*k+2, "D": 2*k+2} 
  return moves[move]

def next_coords(coords, move):
  x, y = coords
  if move == "R":
    return (x+1, y)
  elif move == "U":
    return (x, y+1)
  elif move == "L":
    return (x-1, y)
  elif move == "D":
    return (x, y-1)

def number_spiral_coords(n):
  """Generate a number spiral to find coordinates of number n"""
  move_order = ["R", "U", "L", "D"]
  current_square = 1
  current_block = 0
  current_coords = (0, 0)

  done = False
  while (not done):
    for move in move_order:
      for _ in range(step_length(move, current_block)):
        current_coords = next_coords(current_coords, move)
        current_square += 1
        if current_square == n:
          return current_coords
    current_block += 1

def carry_distance(square):
  x, y = number_spiral_coords(square)
  return abs(x) + abs(y)


assert carry_distance(12) == 3
assert carry_distance(23) == 2
assert carry_distance(1024) == 31

print(carry_distance(312051))


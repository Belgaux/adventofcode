
def checksum(sheet):
  return sum([max(line) - min(line) for line in sheet])

def checksum_div(sheet):
  s = 0
  for line in sheet:
    for num in line:
      for other in line:
        if num != other and num % other == 0:
          s += num / other
  return s


assert checksum([[5,1,9,5], [7,5,3], [2,4,6,8]]) == 18
assert checksum_div([[5,9,2,8], [9,4,7,3], [3,8,6,5]]) == 9

with open("../inputs/02.txt") as f:
  sheet = [line.strip().split("\t") for line in f.readlines()]
  sheet = [[int(e) for e in line] for line in sheet]
  print(checksum(sheet))
  print(checksum_div(sheet))



def checksum(sheet):
  return sum([max(line) - min(line) for line in sheet])


assert checksum([[5,1,9,5], [7,5,3], [2,4,6,8]]) == 18

with open("../inputs/02.txt") as f:
  sheet = [line.strip().split("\t") for line in f.readlines()]
  sheet = [[int(e) for e in line] for line in sheet]
  print(checksum(sheet))


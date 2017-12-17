import collections
import itertools

def valid_passphrase(phrase, part_two=False):
  unique = collections.defaultdict(int)
  for word in phrase.split():
    if part_two:
      unique_permutations = set(itertools.permutations(word))
      for perm in unique_permutations:
        unique[perm] += 1
    else:
      unique[word] += 1
  return all(v is 1 for k, v in unique.items())


with open("../inputs/04.txt") as f:
  puzzle_input = list(line.strip() for line in f)
  print(list((valid_passphrase(line) 
        for line in puzzle_input)).count(True))
  print(list((valid_passphrase(line, part_two=True)
        for line in puzzle_input)).count(True))


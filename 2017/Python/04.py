import collections

def valid_passphrase(phrase):
  unique = collections.defaultdict(int)
  for word in phrase.split():
    unique[word] += 1
  return all(v is 1 for k, v in unique.items())


with open("../inputs/04.txt") as f:
  print(list((valid_passphrase(line) for line in f)).count(True))


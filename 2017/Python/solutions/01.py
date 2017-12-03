
def captcha_sum(seq):
  return sum([int(num) for i, num in enumerate(seq) 
      if seq[i+1 if i < len(seq)-1 else 0] == num])

def captcha_sum_halfway(seq):
  return sum([int(num) for i, num in enumerate(seq) 
      if seq[int((i + len(seq)/2) % len(seq))] == num])



assert(captcha_sum("1122") == 3)
assert(captcha_sum("1111") == 4)
assert(captcha_sum("1234") == 0)
assert(captcha_sum("91212129") == 9)

assert(captcha_sum_halfway("1212") == 6)
assert(captcha_sum_halfway("1221") == 0)
assert(captcha_sum_halfway("123425") == 4)
assert(captcha_sum_halfway("123123") == 12)
assert(captcha_sum_halfway("12131415") == 4)

with open("../inputs/01.txt") as f:
  puzzle_seq = f.read().strip()
  print(captcha_sum(puzzle_seq))
  print(captcha_sum_halfway(puzzle_seq))

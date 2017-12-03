
def captcha_sum(sequence):
  return sum([int(num) for i, num in enumerate(sequence) 
      if sequence[i+1 if i < len(sequence)-1 else 0] == num])


assert(captcha_sum("1122") == 3)
assert(captcha_sum("1111") == 4)
assert(captcha_sum("1234") == 0)
assert(captcha_sum("91212129") == 9)


with open("../inputs/01.txt") as f:
  print(captcha_sum(f.read().strip()))

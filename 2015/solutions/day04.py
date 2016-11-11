import hashlib
import itertools

# testing
a = 'abcdef'
b = '609043'
m = hashlib.md5((a + b).encode()).hexdigest()
print(m[:5] == '00000')

#solution
secret_key = 'bgvyzdsv'
for i in itertools.count(1):
    text = secret_key + str(i)
    b = hashlib.md5(text.encode()).hexdigest()
    # solution part 2 - slice :6 instead of :5 and compare to '000000' instead of '00000'
    if b[:6] == '000000':
        print(i)
        break

def is_triangle(a, b, c):
    return (a + b) > c and (b + c) > a and (a + c) > b

count = 0
for line in open("../inputs/03.txt").readlines():
    args = list(map(int, line.split()))
    if is_triangle(*args):
        print(args)
        count += 1
     
print(count)

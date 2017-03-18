def is_triangle(a, b, c):
    return (a + b) > c and (b + c) > a and (a + c) > b

count = 0
with open("../inputs/03.txt") as fp:
    for line in fp:
        args = list(map(int, line.split()))
        if is_triangle(*args):
            count += 1
print(count)

# part 2
lines = [list(map(int, line.strip().split())) 
            for line in open("../inputs/03.txt")]
count = 0
for col in range(3):
    for i in range(0, len(lines)-2, 3):
        if is_triangle(lines[i][col], 
                lines[i+1][col], 
                lines[i+2][col]):
            count += 1
print(count)

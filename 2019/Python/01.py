def fuel(mass):
    f = (mass // 3) - 2
    if f <= 0:
        return 0
    else:
        return f + fuel(f)

with open("../inputs/01.txt") as f:
    reqs = [int(line.strip()) for line in f.readlines()]
    # p1
    print(sum((mass//3)-2 for mass in reqs))
    # p2
    print(sum(fuel(mass) for mass in reqs))

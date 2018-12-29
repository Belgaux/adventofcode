from collections import defaultdict

with open("../inputs/01.txt") as f_in:
    freqs = list(int(line.rstrip()) for line in f_in.readlines())
    d = defaultdict(int)
    freq = 0
    d[freq] += 1
    found = False
    while not found:
        for frq in freqs:
            freq += frq
            d[freq] += 1
            if d[freq] >= 2:
                print(freq)
                found = True
                break


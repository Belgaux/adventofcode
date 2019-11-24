from collections import Counter
from difflib import ndiff, Differ

with open("../inputs/02.txt") as f:
    candidates = [line.strip() for line in f.readlines()]
    counts = [0, 0]
    for c in candidates:
        d = Counter(c)
        if 3 in d.values():
            counts[0] += 1
        if 2 in d.values():
            counts[1] += 1
    print("Checksum=", counts[0]*counts[1])
    
    for a in candidates:
        for b in candidates:
            res = list(ndiff(a,b))
            if "".join(res).count("+") == 1:
                print("{}\n{}".format(a,b))


from collections import defaultdict
msg = [ line.rstrip() for line in open("../inputs/06.txt").readlines() ]
cols = [ [row[i] for row in msg] for i in range(len(msg[0])) ]

# find char frequency for each column
for col in cols:
    d = defaultdict(int)
    for c in col:
        d[c] += 1
    # part 1
    #print(max(d.items(), key=lambda x: x[1]))
    # part 2
    print(min(d.items(), key=lambda x: x[1]))
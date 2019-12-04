import re

a = 254032
b = 789860
p1, p2 = 0, 0

for i in range(a, b):
    si = str(i)
    m = re.findall(r"((\w)\2{1,})", si)
    if si == "".join(sorted(si)) and m:
        p1 += 1
        if any(len(t[0]) == 2 for t in m):
            p2 += 1

print(p1)
print(p2)


import re
from collections import defaultdict

def is_real(room):
    first_digit = re.search("\d", room).start()
    sector_id = int(room[first_digit:first_digit+3])
    checksum = room[-6:-1]
    name_string = "".join(room[:first_digit-1].split("-"))

    d = defaultdict(int)
    for c in name_string:
        d[c] += 1

    # There is probably a better way to do this?
    # First sort alphabetically to resolve ties
    s1 = sorted(d.items(), key=lambda x: x[0])
    # Then sort by count (which preserves alphabetical order)
    s2 = sorted(s1, key=lambda x: x[1], reverse=True)

    common = "".join([t[0] for t in s2[:5]])
    return common == checksum, sector_id


ids = [is_real(line.strip()) for line in open("../inputs/04.txt")]
real_ids = list(filter(lambda x: x[0] is True, ids))
# Sum of sector IDs of the real rooms
print(sum(t[1] for t in real_ids))


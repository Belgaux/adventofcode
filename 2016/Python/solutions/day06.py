msg = [line.rstrip() for line in open("../inputs/06.txt")]
cols = [[row[i] for row in msg] for i in range(len(msg[0]))]

from collections import Counter
most_common = [Counter(col).most_common()[0] for col in cols]
least_common = [Counter(col).most_common()[-1] for col in cols]

corrected_msg = "".join(x[0] for x in most_common)
corrected_msg_2 = "".join(x[0] for x in least_common)
print(corrected_msg)
print(corrected_msg_2)
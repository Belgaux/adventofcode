import re

with open("../inputs/input19.txt", "r") as fp:
    lines = list(map(str.strip, fp.readlines()))
    tuples = [(t.split()[0], t.split()[2]) for t in lines[:-2]]
    molecule = lines[-1]

def replace_all(s, old, new):
    # Find indices for all occurences of 'old'
    indices = [m.start() for m in re.finditer(old, s)]
    # Build all replacement strings
    return [s[:i] + s[i:].replace(old, new, 1) for i in indices]

# Generate all replacements
molecules = []
for old, new in tuples:
    molecules += replace_all(molecule, old, new)

# Number of distinct molecules
print(len(set(molecules)))


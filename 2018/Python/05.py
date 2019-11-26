from string import ascii_uppercase

def destroy(a, b):
    return (a.isupper() and b == a.lower()) \
            or (a.islower() and b == a.upper())

def react(polymer):
    deleted = True
    while deleted:
        # generate list of deletion candidates
        deletion_candidates = []
        i = 0
        while i < len(polymer):
            try:
                char = polymer[i]
                next_char = polymer[i+1]
            except:
                break
            if destroy(char, next_char):
                deletion_candidates.append(i)
                deletion_candidates.append(i+1)
                i += 2
            else:
                i += 1

        if len(deletion_candidates) > 0:
            # run deletion backwards, highest indices first
            for i in sorted(deletion_candidates, reverse=True):
                del polymer[i]
            deleted = True
        else:
            deleted = False
    
    print("Scan complete.. polymer length=", len(polymer))
    return len(polymer)


with open("../inputs/05.txt") as f:
    input_polymer = f.readlines()
    input_polymer = list(input_polymer[0].strip())

# part 1
print("Length of fully reacted input polymer:", react(input_polymer))

# part 2
polymer_lengths = {}
for c in ascii_uppercase:
    # preprocess polymer, remove all types A/a, B/b, ...
    tmp = "".join(input_polymer)
    tmp = tmp.replace(c, "")
    tmp = tmp.replace(c.lower(), "")
    tmp = list(tmp)
    print("Removed {}/{}".format(c, c.lower()))
    polymer_lengths[c] = react(tmp)

print("Shortest polymer:", min(polymer_lengths.values()))

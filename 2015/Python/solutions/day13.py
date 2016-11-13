def compute_happiness(ordering, table):
    total_happiness = 0
    for i in range(0, len(ordering)):
        person = ordering[i]
        # handle edge case of last element
        if i == len(ordering)-1:
            left = ordering[i-1]
            right = ordering[0]
        else:
            left = ordering[i-1]
            right = ordering[i+1]
        total_happiness += table[(person, left)]
        total_happiness += table[(person, right)]
    return total_happiness    
        
def make_happiness_table(text):
    table = {}
    for line in text:
        if line[2] == "gain":
            table[(line[0], line[10])] = int(line[3])
        else:
            table[(line[0], line[10])] = -int(line[3])
    return table
        
def main():
    """Solution is brute force: 
       1. Make happiness lookup table
       2. Generate all table orderings
       3. Compute happiness for all
       4. Take the biggest
    """
    text = [line.replace(".", "").strip().split() for line in open("../inputs/input13.txt").readlines()]
    happiness_table = make_happiness_table(text)
    people = list(set([line[0] for line in text]))
    
    # part 2
    for p in people:
        happiness_table[("Me", p)] = 0
        happiness_table[(p, "Me")] = 0
    people += ["Me"]
    
    # permutations of table orderings
    from itertools import permutations
    people_permutations = permutations(people)
    h = []
    for perm in people_permutations:
        h.append(compute_happiness(perm, happiness_table))
    print(max(h))
    
    
if __name__ == "__main__":
    main()
    
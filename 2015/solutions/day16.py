def main():
    text = [line.replace(":", "").replace(",", "").strip().split()\
            for line in open("../inputs/input16.txt").readlines()]
    
    sue = {}
    for t in text:
        sue[int(t[1])] = [(t[2], int(t[3])), (t[4], int(t[5])), (t[6], int(t[7]))]
    
    ticker_tape = set([("children", 3), ("cats", 7), ("samoyeds", 2), \
                    ("pomeranians", 3), ("akitas", 0), ("vizslas", 0), \
                    ("goldfish", 5), ("trees", 3), ("cars", 2), ("perfumes", 1)])
    # part 1
    for key, value in sue.items():
        if set(value).issubset(ticker_tape):
            print("Part 1 aunt number: {}".format(key))
    
    # part 2
    # remove invalid tuples
    excluded = ["cats", "trees", "pomeranians", "goldfish"]
    ticker_tape = set([t for t in ticker_tape if t[0] not in excluded])
            
    def real_tuple(t):
        name, number = t
        return (name == "cats" and number > 7) \
            or (name == "trees" and number > 3)\
            or (name == "pomeranians" and number < 3)\
            or (name == "goldfish" and number < 5)\
            or t in ticker_tape
            
    for key, value in sue.items():
        if all([real_tuple(t) for t in value]):
            print("Part 2 aunt number: {}".format(key))
   
    
if __name__ == "__main__":
    main()
    
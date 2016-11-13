def main():
    text = [line.replace(":", "").replace(",", "").strip().split() for line in open("../inputs/input16.txt").readlines()]
    
    sue = {}
    for t in text:
        sue[int(t[1])] = [(t[2], int(t[3])), (t[4], int(t[5])), (t[6], int(t[7]))]
    
    ticker_tape = set([("children", 3), ("cats", 7), ("samoyeds", 2), \
                ("pomeranians", 3), ("akitas", 0), ("vizslas", 0), \
                ("goldfish", 5), ("trees", 3), ("cars", 2), ("perfumes", 1)])
    for key, value in sue.items():
        if set(value).issubset(ticker_tape):
            print(key)
    
    
if __name__ == "__main__":
    main()
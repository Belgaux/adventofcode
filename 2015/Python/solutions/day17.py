def main():
    containers = [int(line.strip()) \
            for line in open("../inputs/input17.txt").readlines()]
    combinations = []
    
    def subset_sum(values, max, partial=[]):
        if sum(partial) == max:
            combinations.append(partial)
        if sum(partial) >= max:
            return
        for i in range(len(values)):
            remaining = values[i + 1:]
            subset_sum(remaining, max, partial + [values[i]])
            
    # part 1
    subset_sum(containers, 150)
    print(len(combinations))
    
    # part 2
    new_combinations = [c for c in combinations \
                        if len(c) == min(map(len, combinations))]
    print(len(new_combinations))
    
                   
if __name__ == "__main__":
    main()
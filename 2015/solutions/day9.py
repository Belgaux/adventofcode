
  
def main():
    """Solution: 
       1. Make a table of all edges with costs
       2. Compute all permutations of paths
       3. Compute costs of permutations
       4. Minimize
       
       Part 2:
       
       ..
       
       4. Maximize 
    """ 
    costs = {}
    locations = []
    # construct edge lookup from input
    with open("../inputs/input9.txt") as f:
        for line in f.readlines():
            args = line.split()
            if args[0] not in locations:
                locations.append(args[0])
            if args[2] not in locations:
                locations.append(args[2])
            # add edge both ways
            costs[(args[0], args[2])] = int(args[4])
            costs[(args[2], args[0])] = int(args[4])
    
    # all permutations
    from itertools import permutations
    all_paths = permutations(locations)

    # compute path costs
    path_costs = []
    for path in all_paths:
        edges = []
        for i in range(0, len(path)-1):
            edges.append((path[i], path[i+1]))
        path_costs += [sum([costs[edge] for edge in edges])]
        
    print("Shortest route: {}".format(min(path_costs)))
    print("Longest route: {}".format(max(path_costs)))
        
        
if __name__ == "__main__":
    main()
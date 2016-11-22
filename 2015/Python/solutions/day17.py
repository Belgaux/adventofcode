def main():
    containers = [int(line.strip()) \
            for line in open("../inputs/input17.txt").readlines()]
    combs = []

    def subset_sum(values, target, partial):
        """Find every subset of values that sum up to target value
        """
        if sum(partial) == target:
            combs.append(partial)
        if sum(partial) >= target:
            return
        for i, value in enumerate(values):
            remaining = values[i + 1:]
            subset_sum(remaining, target, partial + [value])


    # part 1
    subset_sum(containers, 150, [])
    print(len(combs))

    # part 2
    new_combs = [c for c in combs \
                        if len(c) == min(map(len, combs))]
    print(len(new_combs))


if __name__ == "__main__":
    main()

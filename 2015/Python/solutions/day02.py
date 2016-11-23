def surface_area(length, width, height):
    # sort the dimensions
    dims = sorted([length, width, height])
    # get the two smallest numbers
    small = dims[:-1]
    # calculate slack
    slack = small[0] * small[1]
    return 2 * length * width + \
            2 * width * height + \
            2 * length * height + slack

def ribbon_length(length, width, height):
    # sort the dimensions
    dims = sorted([length, width, height])
    # get the two smallest numbers
    small = dims[:-1]
    # calculate ribbon
    ribbon = length * width * height
    return 2 * small[0] + 2 * small[1] + ribbon

def main():
    with open("../inputs/input2.txt") as in_file:
        total_ribbon = 0
        total_surface = 0
        for present in in_file.readlines():
            # get dimensions
            args = [int(dim) for dim in present.split("x")]
            # unpack map into function
            total_ribbon += ribbon_length(args[0], args[1], args[2])
            total_surface += surface_area(args[0], args[1], args[2])
        print("Total feet of ribbon: ", total_ribbon)
        print("Total square feet of paper: ", total_surface)


if __name__ == "__main__":
    main()

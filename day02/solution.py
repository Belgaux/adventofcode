def surface_area(l, w, h):
    # sort the dimensions
    dims = sorted([l, w, h])
    # get the two smallest numbers
    small = dims[:-1]
    # calculate slack
    slack = small[0] * small [1]
    return 2 * l * w + 2 * w * h + 2 * l * h + slack

with open("input.txt") as f:
    total = 0
    for present in f.readlines():
        # get dimensions
        args = map(int, present.split('x'))
        # unpack list into function
        total += surface_area(*args)
    print("Total square feet of paper: ", total)

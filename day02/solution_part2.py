def ribbon_length(l, w, h):
    # sort the dimensions
    dims = sorted([l, w, h])
    # get the two smallest numbers
    small = dims[:-1]
    # calculate ribbon
    ribbon = l * w * h
    return 2 * small[0] + 2 * small[1] + ribbon

with open("input.txt") as f:
    total = 0
    for present in f.readlines():
        # get dimensions
        args = map(int, present.split('x'))
        # unpack map into function
        total += ribbon_length(*args)
    print("Total feet of ribbon: ", total)

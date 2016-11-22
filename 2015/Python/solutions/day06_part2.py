def parse_input(input):
    inst = input.split()
    if "toggle" in inst:
        split_index = (1, 3)
        mode = "toggle"
    else:
        split_index = (2, 4)
        mode = "on" if "on" in inst else "off"
    a, b = split_index
    start = [int(x) for x in inst[a].split(",")]
    stop = [int(x) for x in inst[b].split(",")]
    switch_lights(start, stop, mode)

'''
Only major change in part 2 is in here
'''
def switch_lights(start, stop, mode):
    for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                if mode == "toggle":
                    grid[i][j] += 2
                elif mode == "on":
                    grid[i][j] += 1
                elif mode == "off":
                    if grid[i][j] > 0:
                        grid[i][j] -= 1

def main():
    # initialize grid with brightness 0
    grid = {}
    for i in range(1000):
        grid[i] = [0 for _ in range(1000)]

    with open("../inputs/input6.txt") as f:
        inputs = f.read().splitlines()
    # setup lights
    for input in inputs:
        parse_input(input)
    # calculate total brightness
    brightness = 0
    for i in range(1000):
            for j in range(1000):
                brightness += grid[i][j]
    print("Total brightness: ", brightness)

if __name__ == '__main__':
    main()

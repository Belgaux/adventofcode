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

def switch_lights(start, stop, mode):
    for i in range(start[0], stop[0] + 1):
            for j in range(start[1], stop[1] + 1):
                if mode == "toggle":
                    # fun way to toggle between 1 & 0
                    grid[i][j] = int(not grid[i][j])
                elif mode == "on":
                    grid[i][j] = 1
                elif mode == "off":
                    grid[i][j] = 0

def main():
    # initialize grid with lights off
    grid = {}
    for i in range(1000):
       grid[i] = [0 for _ in range(1000)]
    with open("../inputs/input6.txt") as f:
        inputs = f.read().splitlines()
    # setup lights
    for input in inputs:
        parse_input(input)
    # count number of lights 'on'
    lights_on = 0
    for i in range(1000):
            for j in range(1000):
                if grid[i][j] == 1:
                    lights_on += 1
    print("Lights on count: ", lights_on)

if __name__ == '__main__':
    main()
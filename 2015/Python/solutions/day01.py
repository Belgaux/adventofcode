def main():
    with open("../inputs/input1.txt") as f:
        floor = 0;
        for i, char in enumerate(f.read()):
            # part 2
            if floor == -1:
                print("First floor -1 index: ", i)
                break
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        # part 1
        print(floor)

if __name__ == "__main__":
    main()

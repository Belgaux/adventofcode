
def main():
    with open("../inputs/input8.txt") as f:
        lines = f.read().splitlines()
    # part 1
    # eval() does all the work for me here, converting escape literals and unicode
    print(sum(len(l) - len(eval(l)) for l in lines))
    # part 2
    # add the length + number of literal quotes and backslashes +2 for the surround quotes
    print(sum((len(l) + l.count("\"") + l.count("\\") + 2) - len(l) for l in lines))

if __name__ == '__main__':
    main()

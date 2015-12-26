
def main():
    """
    Get the difference between the length of
    the raw strings and the evaluated strings in memory
    """
    with open("input.txt") as f:
        lines = f.read().splitlines()
    # eval() does all the work for me here, converting escape literals and unicode
    print(sum(len(l) - len(eval(l)) for l in lines))

if __name__ == '__main__':
    main()
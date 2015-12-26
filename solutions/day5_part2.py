import re

# matches a pattern like xyx, efe, aaa, bcb
pattern1 = re.compile(r"(.).\1")
# matches two recurring pairs
pattern2 = re.compile(r"(..).*\1")

def is_nice(string):
    if pattern1.search(string) is None or pattern2.search(string) is None:
        return False
    # true if both patterns match
    return True

def main():
    nice_count = 0
    with open("../inputs/input5.txt") as f:
        for string in f.readlines():
            if is_nice(string):
                nice_count += 1
    print(nice_count)

if __name__ == '__main__':
    main()

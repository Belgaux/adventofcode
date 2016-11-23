import re

# illegal substrings
bad_sub_strings = ["ab", "cd", "pq", "xy"]
# finds substrings of two recurring chars
pattern = re.compile(r"(.)\1{1,}")

# matches a pattern like xyx, efe, aaa, bcb
pattern1 = re.compile(r"(.).\1")
# matches two recurring pairs
pattern2 = re.compile(r"(..).*\1")

def is_nice_day2(string):
    if pattern1.search(string) is None \
            or pattern2.search(string) is None:
        return False
    else:
        return True

def vowel_count(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def is_nice(string):
    for sub in bad_sub_strings:
        if sub in string:
            return False
    return False if (
        vowel_count(string) < 3 or pattern.search(string) is None
    ) else True

def main():
    nice_count = 0
    nice_count_day2 = 0
    with open("../inputs/input5.txt") as f:
        for string in f.readlines():
            if is_nice(string):
                nice_count += 1
            if is_nice_day2(string):
                nice_count_day2 += 1
    print(nice_count)
    print(nice_count_day2)


if __name__ == '__main__':
    main()

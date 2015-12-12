import re

# illegal substrings
bad_sub_strings = ["ab", "cd", "pq", "xy"]
# finds substrings of two recurring chars
pattern = re.compile(r"(.)\1{1,}")

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
    if vowel_count(string) < 3 or pattern.search(string) is None:
        return False
    # true if all tests pass
    return True

def main():
    nice_count = 0
    with open("input.txt") as f:
        for string in f.readlines():
            if is_nice(string):
                nice_count += 1
    print(nice_count)

if __name__ == '__main__':
    main()

from itertools import groupby

def main():
    """Look-and-say sequences
       we want a new string on the form:
       'number of copies' of 'some digit' ... for each group of consecutive digits
       112 becomes 2112 (two ones, one two)
    """
    def look_and_say(string):
        # itertools.groupby returns groups of consecutive keys from an iterable
        return "".join([str(len(list(group))) + key for key, group in groupby(string)])

    s = "1113222113"
    for n in range(50):
        s = look_and_say(s)
    print(len(s))


if __name__ == "__main__":
    main()

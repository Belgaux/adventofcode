
def main():
    total_char_num = 0
    with open("input.txt") as f:
        text = f.read().splitlines()
    for line in text:
        # add the untouched char code count
        total_char_num += len(line)
        s = line[1:-1]
        print(s)
        print(len(s))
        # temporarily subtract everything
        total_char_num -= len(s)
        # add back the unicode conversions and escaped codes
        for i in range(len(s)-1):
            print(i,s[i:i+2])
            if s[i:i+2] == "\\x":
                # 4 chars become 1 unicode char, add difference
                print(True)
                total_char_num += 3
            # escaping a backslash might happen
            elif s[i] == "\\" and s[i+1] != ("x" or "\\"):
                print(True)
                total_char_num += 1

        # remove escape characters
    print(total_char_num)


if __name__ == '__main__':
    main()
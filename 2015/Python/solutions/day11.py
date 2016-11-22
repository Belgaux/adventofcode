def three_increasing_letters(password):
    for i in range(1, len(password)-1):
        if ord(password[i])-1 == ord(password[i-1]) and ord(password[i])+1 == ord(password[i+1]):
            return True
    return False

def contains_valid_letters(password):
    if "i" in password or "o" in password or "l" in password:
            return False
    return True

def two_pairs(password):
    # find first pair
    for i in range(0, len(password)-1):
        if password[i] == password[i+1]:
            # find second pair
            for j in range(i+2, len(password)-1):
                if password[j] == password[j+1]:
                    return True
    return False

def valid_password(password):
    return three_increasing_letters(password) and contains_valid_letters(password) and two_pairs(password)

def increment_string(string):
    chars = list(string)
    # increment character
    chars[-1] = chr(ord(chars[-1]) + 1)
    # check overflow
    for i in range(-1, -len(chars), -1):
        if ord(chars[i]) == ord("z")+1:
            chars[i] = "a"
            chars[i-1] = chr(ord(chars[i-1]) + 1)
    return "".join(chars)

def main():
    # part 1
    password = "hepxcrrq"
    while not valid_password(password):
        password = increment_string(password)
    print("Part 1 answer: {}".format(password))

    # part 2: next valid password
    password = increment_string(password)
    while not valid_password(password):
        password = increment_string(password)
    print("Part 2 answer: {}".format(password))

if __name__ == "__main__":
    main()

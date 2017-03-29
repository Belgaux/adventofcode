import hashlib

i = 0
puzzle_input = "abbhdwsy"
password = []
password_two = [None]*8

while (True):
    door_hash = hashlib.md5(bytes(puzzle_input + str(i), encoding="UTF-8")).hexdigest()
    if door_hash[:5] == "00000":
        password.append(door_hash[5])
        try:
            if password_two[int(door_hash[5])] is None:
                password_two[int(door_hash[5])] = door_hash[6]
            print(password_two)
        except:
            pass
    if all(p is not None for p in password_two):
        break
    i += 1

print("".join(password))
print("".join(password_two))


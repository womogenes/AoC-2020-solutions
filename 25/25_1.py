with open("25_input.txt") as fin:
    data = fin.read().split("\n")

MOD = 20201227

def find_loop_size(subject, public_key):
    for i in range(MOD):
        if pow(subject, i, MOD) == public_key:
            return i

    return -1

card_public = int(data[0])
door_public = int(data[1])

card_loop_size = find_loop_size(7, card_public)
print(pow(door_public, card_loop_size, MOD))
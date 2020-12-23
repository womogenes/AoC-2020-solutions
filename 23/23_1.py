with open("23_input.txt") as fin:
    data = fin.read()

def simulate_move(cups, current):
    n = len(cups)
    
    picked_up = []
    index = (cups.index(current) + 1) % n
    
    for _ in range(3):
        picked_up.append(cups[index])
        index = (index + 1) % n

    for i in picked_up:
        cups.remove(i)

    dest = current - 1
    while dest not in cups:
        dest = dest - 1
        if dest < min(cups):
            dest = max(cups)

    dest_index = cups.index(dest)
    insert_index = (dest_index + 1) % n

    cups = cups[:insert_index] + picked_up + cups[insert_index:]
    new_current_index = (cups.index(current) + 1) % n

    return cups, cups[new_current_index]

cups = [int(i) for i in list(data)]
current = cups[0]

for _ in range(100):
    cups, current = simulate_move(cups, current)

cups.remove(1)
print("".join([str(i) for i in cups]))
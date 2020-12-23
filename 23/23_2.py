with open("23_input.txt") as fin:
    data = fin.read()

def simulate_move(current):
    removed = []
    removed.append(nc[current])
    for _ in range(2):
        removed.append(nc[removed[-1]])

    # Fix the gap
    nc[current] = nc[removed[-1]]

    dest = current - 1
    while dest in removed or dest == 0:
        dest -= 1
        if dest < 1:
            dest = n

    nc[removed[-1]] = nc[dest]
    nc[dest] = removed[0]

    return nc[current]

# Number of cups
n = 10 ** 6

# Sort of like a linked list
# nc stands for "next cup"
nc = [-1] * (n + 1)

cups = [int(i) for i in list(data)]

for i in range(len(cups) - 1):
    nc[cups[i]] = cups[i + 1]
nc[cups[-1]] = max(cups) + 1

for i in range(max(cups) + 1, n):
    nc[i] = i + 1
nc[n] = cups[0]


current = cups[0]

for i in range(10 ** 7):
    current = simulate_move(current)

# Find the two cups to the right of cup 1
first = nc[1]
second = nc[first]
print(first, second)
print(first * second)
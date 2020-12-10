with open("10-input.txt") as fin:
    data = fin.read()

def count_differences(joltages):
    joltages.sort()
    ones = 0
    threes = 0

    #print(joltages)

    for i in range(len(joltages) - 1):
        #print(joltages[i], joltages[i + 1])

        diff = joltages[i + 1] - joltages[i]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    return ones, threes + 1

# NOT CONSIDERING OUR DEVICE
joltages = [0] + [int(i) for i in data.split("\n")]

ones, threes = count_differences(joltages)
print(ones * threes)
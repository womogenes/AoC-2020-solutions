with open("9-input.txt") as fin:
    data = fin.read()

def firstInvalid(sequence, preambleLength):
    for i in range(preambleLength, len(sequence)):
        num = sequence[i]
        # Find two numbers in the previous preambleLength numbers that sum to num
        found = False

        for j in range(i - preambleLength, i):
            for k in range(j, i):
                if sequence[j] + sequence[k] == num:
                    found = True
                    break

            if found:
                break

        if not found:
            return num

    return -1

sequence = [int(i) for i in data.split("\n")]
ans = firstInvalid(sequence, 25)
print(ans)
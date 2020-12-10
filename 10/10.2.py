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
invalidNum = firstInvalid(sequence, 25)

# Create a list of prefix sums to speed up computation
prefixSums = [0]
for i in sequence:
    prefixSums.append(prefixSums[-1] + i)

for i in range(len(sequence)):
    for j in range(i + 1, len(sequence)):
        rangeSum = prefixSums[j + 1] - prefixSums[i]
        if rangeSum == invalidNum:
            low = min(sequence[i:j + 1])
            hi = max(sequence[i:j + 1])
            print(low + hi)
            break
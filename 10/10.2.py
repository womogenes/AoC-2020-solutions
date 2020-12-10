from functools import lru_cache

with open("10-input.txt") as fin:
    data = fin.read()

joltages = [0] + [int(i) for i in data.split("\n")]
joltages.sort()

# Number of ways to connect to device given a source of joltates[index]
@lru_cache(None)
def dp(index):
    #print(index)

    if index == len(joltages) - 1:
        return 1

    total = 0
    nextIndex = index + 1
    #print(index, nextIndex)
    while nextIndex < len(joltages) and joltages[nextIndex] - joltages[index] <= 3:
        total += dp(nextIndex)
        nextIndex += 1

    return total

ans = dp(0)
print(ans)
with open("15_input.txt") as fin:
    data = fin.read()

def sequence(starting, n):
    # Get the nth number of the sequence starting with given starting list

    lastSpoken = {}
    lastLastSpoken = {}

    # Counts how many numbers have been spoken so far
    spokenCount = 0
    
    for num in starting:
        spokenCount += 1
        if num in lastSpoken:
            lastLastSpoken[num] = lastSpoken[num]
        lastSpoken[num] = spokenCount

    # Tracks previous number said
    prev = num

    while spokenCount < n:
        spokenCount += 1

        if prev in lastLastSpoken:
            cur = lastSpoken[prev] - lastLastSpoken[prev]
        else:
            cur = 0

        if cur in lastSpoken:
            lastLastSpoken[cur] = lastSpoken[cur]
        lastSpoken[cur] = spokenCount

        prev = cur

    return prev


starting = [int(i) for i in data.split(",")]
ans = sequence(starting, 30 * 10 ** 6)

print(ans)
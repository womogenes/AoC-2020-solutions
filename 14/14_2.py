import collections
import itertools

with open("14_input.txt") as fin:
    data = fin.read()

def run(program):
    # Runs the program, which is a list of commands
    # Returns a dictionary (map)
    memory = collections.defaultdict(int)

    for line in program:
        parts = line.split(" ")

        if line.startswith("mem"):
            addr = int(parts[0][parts[0].index("[") + 1:parts[0].index("]")])
            value = int(parts[2])

            # Decode the address instead of the value
            bits = list(bin(addr)[2:].zfill(36))

            # Apply the bitmask
            xCount = 0
            for i in range(36):
                # An "X" means the bit is floating
                if mask[i] in ["1", "X"]:
                    bits[i] = mask[i]
                    xCount += mask[i] == "X"

            perms = itertools.product(("1", "0"), repeat=xCount)
            for perm in perms:
                # Modify the bits in the address
                bitsCopy = bits.copy()
                xIndex = 0
                for i in range(36):
                    if bitsCopy[i] == "X":
                        bitsCopy[i] = perm[xIndex]
                        xIndex += 1

                # Interpret the new address into base 2
                newAddr = int("".join(bitsCopy), 2)
                memory[newAddr] = value


        elif line.startswith("mask"):
            mask = parts[2]

    return memory


program = data.split("\n")
ans = run(program)

# Sum all non-zero values
s = 0
for addr in ans:
    s += ans[addr]

print(s)
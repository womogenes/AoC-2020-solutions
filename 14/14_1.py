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
            bits = list(bin(value)[2:].zfill(36))

            # Apply the bitmask
            for i in range(36):
                if mask[i] in ["0", "1"]:
                    bits[i] = mask[i]

            # Interpret the new value into base 2
            newValue = int("".join(bits), 2)
            memory[addr] = newValue


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
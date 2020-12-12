with open("8-input.txt") as fin:
    data = fin.read()

program = data.split("\n")

def run(program):
    accumulator = 0
    pointer = 0

    def execute(instruction):
        op, arg = instruction.split(" ")
        if op == "acc":
            return int(arg), 1

        elif op == "jmp":
            return 0, int(arg)

        else:
            return 0, 1
    
    
    seen = set() # Set of pointers we've seen so far
    accumulator = 0
    pointer = 0
    while pointer not in seen and pointer < len(program):
        seen.add(pointer)
        acc, jmp = execute(program[pointer])
        accumulator += acc
        pointer += jmp

    if pointer >= len(program):
        return accumulator

    return None


# BASH BASH BASH
for i in range(len(program)):
    if program[i].startswith("acc"):
        continue

    if program[i].startswith("nop"):
        copy = program.copy()
        copy[i] = "jmp" + copy[i][3:]

    else:
        copy = program.copy()
        copy[i] = "nop" + copy[i][3:]
    
    x = run(copy)
    if x:
        print(x)
        break
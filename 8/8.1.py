with open("8-input.txt") as fin:
    data = fin.read()

program = data.split("\n")

accumulator = 0
pointer = 0

def execute(instruction):
    global accumulator
    global pointer

    op, arg = instruction.split(" ")
    if op == "acc":
        accumulator += int(arg)
        pointer += 1

    elif op == "jmp":
        pointer += int(arg)

    else:
        pointer += 1

seen = set() # Set of pointers we've seen so far
while pointer not in seen:
    seen.add(pointer)
    execute(program[pointer])

print(accumulator)
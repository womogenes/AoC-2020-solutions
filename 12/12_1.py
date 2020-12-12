with open("12_input.txt") as fin:
    data = fin.read()

directions = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0)
}

def displacement(instructions):
    direction = 0 # Facing east

    # 0 is east, 90 is north, 180 is west, 270 is south

    dx = 0
    dy = 0

    for i in instructions:
        action = i[0]
        amount = int(i[1:])

        # Case if action is one of N, S, E, or W
        if action in directions:
            x, y = directions[action]
            dx += x * amount
            dy += y * amount

        elif action == "L":
            direction = (direction + amount) % 360
        elif action == "R":
            direction = (direction - amount) % 360

        else:
            if direction == 0:
                dx += amount
            elif direction == 90:
                dy += amount
            elif direction == 180:
                dx -= amount
            elif direction == 270:
                dy -= amount

    return dx, dy        

instructions = data.split("\n")
dx, dy = displacement(instructions)
print(dx, dy)

ans = abs(dx) + abs(dy)
print(ans)
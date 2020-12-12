with open("12_input.txt") as fin:
    data = fin.read()

directions = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0)
}

def displacement(instructions):
    # Location of the waypoint
    wx = 10
    wy = 1

    # Location of the ship
    dx = 0
    dy = 0

    for i in instructions:
        action = i[0]
        amount = int(i[1:])

        # Case if action is one of N, S, E, or W
        if action in directions:
            x, y = directions[action]
            wx += x * amount
            wy += y * amount

        elif action in ["L", "R"]:
            if (action == "L" and amount == 90) or (action == "R" and amount == 270):
                wx, wy = -wy, wx
            elif amount == 180:
                wx, wy = -wx, -wy
            elif (action == "L" and amount == 270) or (action == "R" and amount == 90):
                wx, wy = wy, -wx

        else:
            dx += wx * amount
            dy += wy * amount

    return dx, dy

instructions = data.split("\n")
dx, dy = displacement(instructions)
print(dx, dy)

ans = abs(dx) + abs(dy)
print(ans)
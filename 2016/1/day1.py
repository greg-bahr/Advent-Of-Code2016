input = open("input.txt", "r").read().split(", ")

x = 0
y = 0



directions = ["north", "east","south", "west"]
direction = directions[0]

locs = []

for instruction in input:
    if instruction[0] == "R":
        direction = directions[(directions.index(direction) + 1)%4]
    elif instruction[0] == "L":
        direction = directions[(directions.index(direction) - 1)%4]

    for place in range(int(instruction[1:])):
            if direction == "north":
                locs.append((x, y+place))
            elif direction == "south":
                locs.append((x, y-place))
            elif direction == "west":
                locs.append((x-place, y))
            elif direction == "east":
                locs.append((x+place, y))


    if direction == "north":
        y += int(instruction[1:])
    elif direction == "south":
        y -= int(instruction[1:])
    elif direction == "west":
        x -= int(instruction[1:])
    elif direction == "east":
        x += int(instruction[1:])



for loc in locs:
    if locs.count(loc) > 1:
        print loc
        break

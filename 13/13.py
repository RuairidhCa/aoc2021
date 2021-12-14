with open("input.txt") as f:
    input = f.read().splitlines()


points = set()

instructions = []

max_x = max_y = 0
for line in input:
    if line.startswith("fold along "):
        instruction = line.replace("fold along ", "").split("=")
        instruction[1] = int(instruction[1])
        instructions.append(instruction)
    elif line != "":
        point = line.split(",")
        point = [int(coord) for coord in point]
        points.add(tuple(point))


def fold_paper(instruction, points):
    axis, value = instruction
    new_points = set()

    global max_x, max_y

    for point in points:
        if axis == "y":
            y = value - (point[1] - value) if point[1] > value else point[1]
            new_points.add((point[0], y))
            max_y = value
        if axis == "x":
            x = value - (point[0] - value) if point[0] > value else point[0]
            new_points.add((x, point[1]))
            max_x = value
    return new_points


def part_one(points=points):
    points = fold_paper(instructions[0], points)
    print(len(points))


def part_two(points=points):
    global max_x, max_y

    for instruction in instructions:
        points = fold_paper(instruction, points)

    grid = [[" "] * (max_x + 1) for i in range(max_y + 1)]

    for point in points:
        x, y = point
        grid[y][x] = "#"

    for line in grid:
        print("".join(line))


part_one()
part_two()

import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()

grid = np.array([[int(num) for num in i] for i in input])
grid_x, grid_y = grid.shape


def get_adjacent_locations(i, j):
    adj = []
    for x in range(i - 1, i + 2):
        if x < 0 or x >= grid_x:
            continue
        for y in range(j - 1, j + 2):
            if y < 0 or y >= grid_y:
                continue
            adj.append({"value": grid[x][y], "pos": [x, y]})
    return adj


def flash(i, j, flashed=[]):
    flashed.append([i, j])
    adj = [
        x["pos"]
        for x in get_adjacent_locations(i, j)
        if x["pos"] not in flashed and x["value"] <= 9
    ]
    if adj == []:
        return
    else:
        for point in adj:
            i, j = point
            grid[i][j] += 1

            if grid[i][j] > 9:
                if [i, j] not in flashed:
                    flash(i, j, flashed)


def part_one(steps=100):
    flashed_count = 0
    while steps:
        flashed = []
        for i, _ in enumerate(grid):
            for j, _ in enumerate(_):
                grid[i][j] += 1

                if grid[i][j] > 9:
                    if [i, j] not in flashed:
                        flash(i, j, flashed)

        for i, j in flashed:
            grid[i][j] = 0

        flashed_count += len(flashed)
        steps -= 1
    print(flashed_count)


def part_two():
    step_count = 0
    keep_going = True
    while keep_going:
        flashed = []
        for i, _ in enumerate(grid):
            for j, _ in enumerate(_):
                grid[i][j] += 1

                if grid[i][j] > 9:
                    if [i, j] not in flashed:
                        flash(i, j, flashed)

        for i, j in flashed:
            grid[i][j] = 0

        step_count += 1
        total_octopuses = grid_x * grid_y
        keep_going = len(flashed) != total_octopuses
    print(step_count)


# part_one()
part_two()

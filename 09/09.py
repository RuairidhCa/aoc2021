import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()

grid = np.array([[int(num) for num in row] for row in input])
grid_x, grid_y = grid.shape


def get_adjacent_locations(row, column):
    adj = []
    if row - 1 >= 0:
        adj.append({"value": grid[row - 1][column], "pos": [row - 1, column]})
    if column + 1 < grid_y:
        adj.append({"value": grid[row][column + 1], "pos": [row, column + 1]})
    if row + 1 < grid_x:
        adj.append({"value": grid[row + 1][column], "pos": [row + 1, column]})
    if column - 1 >= 0:
        adj.append({"value": grid[row][column - 1], "pos": [row, column - 1]})

    return adj


def get_low_points():
    low_points = []
    for row in range(grid_x):
        for column in range(grid_y):
            adjacent_locations = get_adjacent_locations(row, column)
            adjacent_values = [location["value"] for location in adjacent_locations]

            if all(x > grid[row][column] for x in adjacent_values):
                low_points.append({"value": grid[row][column], "pos": [row, column]})
    return low_points


def part_one():
    low_points = get_low_points()
    low_point_values = [location["value"] for location in low_points]
    print(f"Total Risk Level: {sum(low_point_values) + len(low_points)}")


def get_basin(current_point, visited=[]):
    if type(current_point) is not list:
        current_point = current_point["pos"]

    visited.append(current_point)
    row, column = current_point
    adj = [
        x["pos"]
        for x in get_adjacent_locations(row, column)
        if x["value"] != 9 and x["pos"] not in visited
    ]
    visited += adj
    if adj == []:
        return [current_point]
    else:
        return_value = [current_point]
        return_value += [y for point in adj for y in get_basin(point)]

        return return_value


def part_two():
    low_points = get_low_points()
    basin_list = []
    for low_point in low_points:
        basin_list.append(get_basin(low_point))
    basin_list.sort(key=len)
    largest_basins = [len(basin) for basin in basin_list][-3:]
    print(f"Result: {np.prod(largest_basins)}")


# part_one()
part_two()

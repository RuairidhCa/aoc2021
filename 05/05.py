with open("input.txt") as f:
    input = f.read().splitlines()

lines = [line.split(" -> ") for line in input]
max_x = max([int(point.split(",")[0]) for line in lines for point in line]) + 1
max_y = max([int(point.split(",")[1]) for line in lines for point in line]) + 1
grid = [[0 for y in range(max_y)] for x in range(max_x)]


def part_one():
    for line in lines:
        points = [point.split(",") for point in line]
        points = [int(value) for point in points for value in point]
        x1, y1, x2, y2 = points
        if x1 == x2:
            start = min(y1, y2)
            stop = max(y1, y2) + 1
            points_to_plot = [[x1, y] for y in list(range(start, stop))]
            for x, y in points_to_plot:
                grid[x][y] += 1
        if y1 == y2:
            start = min(x1, x2)
            stop = max(x1, x2) + 1
            points_to_plot = [[x, y1] for x in list(range(start, stop))]
            for x, y in points_to_plot:
                grid[x][y] += 1

    count_overlaps = len([row for column in grid for row in column if row >= 2])

    print(count_overlaps)


def part_two():
    for line in lines:
        points = [point.split(",") for point in line]
        points = [int(value) for point in points for value in point]
        x1, y1, x2, y2 = points
        if x1 == x2:
            start = min(y1, y2)
            stop = max(y1, y2) + 1
            points_to_plot = [[x1, y] for y in list(range(start, stop))]
            for x, y in points_to_plot:
                grid[x][y] += 1
        if y1 == y2:
            start = min(x1, x2)
            stop = max(x1, x2) + 1
            points_to_plot = [[x, y1] for x in list(range(start, stop))]
            for x, y in points_to_plot:
                grid[x][y] += 1
        if x1 - y1 == x2 - y2:
            start_x = min(x1, x2)
            stop_x = max(x1, x2) + 1
            start_y = min(y1, y2)
            stop_y = max(y1, y2) + 1
            points_to_plot_x = list(range(start_x, stop_x))
            points_to_plot_y = list(range(start_y, stop_y))
            points_to_plot = list(zip(points_to_plot_x, points_to_plot_y))
            for x, y in points_to_plot:
                grid[x][y] += 1
        if x1 + y1 == x2 + y2:
            start_x = min(x1, x2)
            stop_x = max(x1, x2) + 1
            start_y = min(y1, y2)
            stop_y = max(y1, y2) + 1
            points_to_plot_x = list(range(start_x, stop_x))
            points_to_plot_y = list(range(start_y, stop_y))
            points_to_plot_y.reverse()
            points_to_plot = list(zip(points_to_plot_x, points_to_plot_y))
            for x, y in points_to_plot:
                grid[x][y] += 1

    count_overlaps = len([row for column in grid for row in column if row >= 2])

    print(count_overlaps)


# part_one()
part_two()

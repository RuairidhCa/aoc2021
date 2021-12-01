with open("input.txt") as f:
    measurements = f.readlines()

measurements = [int(measurement.strip()) for measurement in measurements]


def part_one():
    count = 0
    previous_measurement = None
    for measurement in measurements:
        current_measurement = measurement
        if (
            previous_measurement is not None
            and current_measurement > previous_measurement
        ):
            count += 1
        previous_measurement = current_measurement

    print(count)


def part_two():
    window_start = 0
    window_end = window_start + 3
    count = 0
    while window_start < len(measurements) - 3:
        window_a = measurements[window_start:window_end]
        window_b = measurements[window_start + 1 : window_end + 1]
        if sum(window_a) < sum(window_b):
            count += 1
        window_start += 1
        window_end += 1

    print(count)


part_one()
part_two()

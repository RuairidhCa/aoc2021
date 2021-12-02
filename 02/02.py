with open("input.txt") as f:
    commands = f.readlines()

commands = [command.strip() for command in commands]



def part_one():
    horizontal_position = 0
    depth = 0
    for command in commands:
        (direction, value) = command.split()
        value = int(value)
        match direction:
            case "forward":
                horizontal_position += value
            case "up":
                depth -= value
            case "down":
                depth += value
            case _:
                pass
        print(f"horizontal_position: {horizontal_position}")
        print(f"depth: {depth}")
        print(f"horizontal_position * depth: {horizontal_position * depth}")


def part_two():
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        (direction, value) = command.split()
        value = int(value)
        match direction:
            case "forward":
                horizontal_position += value
                depth += (aim*value)
            case "up":
                aim -= value
            case "down":
                aim += value
            case _:
                pass
    print(f"horizontal_position: {horizontal_position}")
    print(f"depth: {depth}")
    print(f"horizontal_position * depth: {horizontal_position * depth}")


part_one()
part_two()

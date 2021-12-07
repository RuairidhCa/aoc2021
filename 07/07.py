from statistics import median, mean
from math import floor

with open("input.txt") as f:
    input = f.read().split(",")

input = [int(num) for num in input]


def part_one():
    input.sort()
    median_pos = int(median(input))
    distances = [abs(pos - median_pos) for pos in input]
    fuel_required = sum(distances)
    print(f"Fuel required: {fuel_required}")


def part_two():
    mean_pos = floor(mean(input))
    distances = [abs(pos - mean_pos) for pos in input]
    fuel = [distance * (distance + 1) / 2 for distance in distances]
    fuel_required = int(sum(fuel))
    print(f"Fuel required: {fuel_required}")


part_one()
part_two()

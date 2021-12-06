with open("input.txt") as f:
    input = f.read()

ages = [int(age) for age in input.split(",")]


class Lanternfish:
    def __init__(self, age=8):
        self.age = age

    def decrementAge(self):
        if self.age == 0:
            self.age = 6
        else:
            self.age -= 1

    def __repr__(self):
        return f"{self.age}"


def part_one(target_days):
    lanternfish_list = [Lanternfish(age) for age in ages]

    days = range(0, target_days)
    for day in days:
        print(day)
        new_lanternfish = []
        for lanternfish in lanternfish_list:
            if lanternfish.age == 0:
                new_lanternfish.append(Lanternfish())

            lanternfish.decrementAge()
        lanternfish_list += new_lanternfish
    print(
        f"Number of Lanternfish after {target_days} day{'s' if target_days!=1 else ''}: {len(lanternfish_list)}"
    )


def part_two(target_days):
    lanternfish_ages = {num: 0 for num in range(9)}
    for age in ages:
        lanternfish_ages[age] += 1

    days = range(0, target_days)
    for day in days:
        num_new_fish = lanternfish_ages[0]
        for age in lanternfish_ages.keys():
            if age == 8:
                lanternfish_ages[age] = num_new_fish
            elif age == 6:
                lanternfish_ages[age] = num_new_fish + lanternfish_ages[age + 1]
            else:
                lanternfish_ages[age] = lanternfish_ages[age + 1]

    print(
        f"Number of Lanternfish after {target_days} day{'s' if target_days!=1 else ''}: {sum(lanternfish_ages.values())}"
    )


# part_one(80)
part_two(256)

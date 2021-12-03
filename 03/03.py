with open("input.txt") as f:
    numbers = f.readlines()

numbers = [number.strip() for number in numbers]
number_of_bits = len(numbers[0])


def part_one():
    gamma_rate = ""
    epsilon_rate = ""

    for j in range(number_of_bits):
        count_0 = 0
        count_1 = 0

        for i in range(len(numbers)):
            if numbers[i][j] == "0":
                count_0 += 1
            elif numbers[i][j] == "1":
                count_1 += 1

        if count_0 > count_1:
            gamma_rate += "0"
            epsilon_rate += "1"
        elif count_0 < count_1:
            gamma_rate += "1"
            epsilon_rate += "0"

    print("--------")
    print(f"Gamma rate: {int(gamma_rate, 2)}")
    print(f"Epsilon rate: {int(epsilon_rate, 2)}")
    print(f"Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")
    print("--------")


def get_rating(type):
    rating_list = numbers
    for j in range(number_of_bits):
        count_0 = 0
        count_1 = 0

        for i in range(len(rating_list)):
            if rating_list[i][j] == "0":
                count_0 += 1
            elif rating_list[i][j] == "1":
                count_1 += 1

        primary_bit = "1" if type == "c02" else "0"
        secondary_bit = "0" if type == "c02" else "1"

        if count_0 > count_1:
            rating_list = list(filter(lambda num: num[j] == primary_bit, rating_list))
        elif count_0 <= count_1:
            rating_list = list(filter(lambda num: num[j] == secondary_bit, rating_list))

        if len(rating_list) == 1:
            return int(rating_list[0], 2)


def part_two():
    c02_rating = get_rating("c02")
    oxy_rating = get_rating("oxy")
    print(f"Oxygen Generator Rating: {oxy_rating}")
    print(f"C02 Scrubber Rating: {c02_rating}")
    print(f"Life Support Rating: {oxy_rating * c02_rating}")
    print("--------")


part_one()
part_two()

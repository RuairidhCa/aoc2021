from math import floor

with open("input.txt") as f:
    input = f.read().splitlines()


char_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
illegal_score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_score_map = {")": 1, "]": 2, "}": 3, ">": 4}


def part_one():
    score = 0
    for line in input:
        stack = []
        for char in line:
            if char in char_map.keys():
                stack.append(char)
            elif char in char_map.values():
                expected_char = char_map[stack[-1]]
                if expected_char != char:
                    print(f"Expected {expected_char}, but found {char} instead.")

                    score += illegal_score_map[char]
                    break
                else:
                    stack.pop()
    print(f"Total syntax error score: {score}")


def part_two():
    scores = []
    for line in input:
        stack = []
        for char in line:
            if char in char_map.keys():
                stack.append(char)
            elif char in char_map.values():
                expected_char = char_map[stack[-1]]
                if expected_char != char:
                    print(f"Expected {expected_char}, but found {char} instead.")
                    break
                else:
                    stack.pop()
        else:
            stack.reverse()
            stack = [char_map[char] for char in stack]
            line_score = 0
            for char in stack:
                line_score *= 5
                line_score += incomplete_score_map[char]
            print(f"Completion string score: {line_score}")
            scores.append(line_score)
    scores.sort()
    middle_index = floor(len(scores) / 2)
    print(f"Winning score: {scores[middle_index]}")


part_one()
part_two()

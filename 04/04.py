from pprint import pprint

with open("input.txt") as f:
    input = f.read().splitlines()

draw_numbers = input.pop(0).split(",")

boards = []
new_board = []
for line in input:
    if len(line.strip()) == 0:
        if new_board != []:
            boards.append(
                {
                    "board": new_board,
                    "row": [0, 0, 0, 0, 0],
                    "col": [0, 0, 0, 0, 0],
                    "marked": [],
                }
            )
            new_board = []
    else:
        new_board.append(line.split())

boards.append(
    {"board": new_board, "row": [0, 0, 0, 0, 0], "col": [0, 0, 0, 0, 0], "marked": []}
)


def part_one():
    winning_board = None
    for number in draw_numbers:
        if winning_board:
            break
        for board in boards:
            for row_index, row in enumerate(board["board"]):
                if number in row:
                    board["row"][row_index] += 1
                    board["col"][row.index(number)] += 1
                    board["marked"].append(int(number))
            if 5 in board["row"] or 5 in board["col"]:
                winning_board = board
                winning_number = int(number)

    flat_board = [int(number) for row in winning_board["board"] for number in row]
    unmarked_numbers = list(
        filter(lambda num: num not in winning_board["marked"], flat_board)
    )
    print(sum(unmarked_numbers) * winning_number)


def part_two():
    winning_boards = []
    for number in draw_numbers:
        if len(winning_boards) == len(boards):
            break
        for board in boards:
            for row_index, row in enumerate(board["board"]):
                if number in row:
                    board["row"][row_index] += 1
                    board["col"][row.index(number)] += 1
                    board["marked"].append(int(number))
            if 5 in board["row"] or 5 in board["col"]:
                if board not in winning_boards:
                    winning_boards.append(board)
                winning_number = int(number)

    last_winning_board = winning_boards.pop()
    flat_board = [int(number) for row in last_winning_board["board"] for number in row]
    unmarked_numbers = list(
        filter(lambda num: num not in last_winning_board["marked"], flat_board)
    )
    print(sum(unmarked_numbers) * winning_number)


part_one()
part_two()

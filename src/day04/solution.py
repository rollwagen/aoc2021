def _print(message: str):
    print(f"[DEBUG] {message}")


boards = []

input = [line.strip() for line in open("input").readlines()]
# input = [line.strip() for line in open("input.sample").readlines()]

# first line of input is 'bingo' draw numbers
draw_numbers = [int(n) for n in input[0].split(",")]
_print(f"{draw_numbers=}")

# empty line separates draw numbers from board input
# each board 5 lines separated by newline
input_boards = input[2:]
index = 0
max_index = len(input_boards) - 5
while index <= max_index:
    board = []
    for board_index in range(5):
        board_line = [int(n) for n in input_boards[index + board_index].split()]
        # board[board_index] = board_line
        board.append(board_line)
    boards.append(board)
    index += 5 + 1  # don't forget empty line
_print(f"{boards=}")

already_called_numbers = set()
boards_already_won = set()
first_winning_board_score = -1
for current_draw in draw_numbers:  # noqa: C901

    already_called_numbers.add(current_draw)
    first_winning_board = None

    # check each board if it has a match
    for board_index, board in enumerate(boards):

        # check for horizontal match
        for row in board:
            horizontal_matches = sum(True for n in row if n in already_called_numbers)
            if horizontal_matches == 5:
                if not first_winning_board:
                    first_winning_board = boards[board_index]
                boards_already_won.add(board_index)

        # check for vertical match
        for col in map(list, zip(*board)):
            vertical_matches = sum(True for n in col if n in already_called_numbers)
            if vertical_matches == 5:
                if not first_winning_board:
                    first_winning_board = boards[board_index]
                boards_already_won.add(board_index)

        if len(boards_already_won) == len(boards):
            last_winning_board = boards[board_index]
            sum_unmarked = 0
            for row in last_winning_board:
                sum_unmarked += sum(n for n in row if n not in already_called_numbers)
            last_winning_board_score = sum_unmarked * current_draw
            _print(f"last winning board score {last_winning_board_score=}")
            exit(0)

        if first_winning_board and first_winning_board_score < 0:
            _print(f"{first_winning_board=}")
            # calculate score:
            # 1 - sum of all unmarked numbers
            sum_unmarked = 0
            for row in first_winning_board:
                sum_unmarked += sum(n for n in row if n not in already_called_numbers)
            # 2 - multiply the sum by the number that was just called
            first_winning_board_score = sum_unmarked * current_draw
            _print(f"first winning board score: {first_winning_board_score}")


def part_one() -> int:
    pass


def part_two() -> int:
    pass


if __name__ == "__main__":
    print(f"{part_one()=}  32844 (sample: 4512)")
    print(f"{part_two()=}  4920 (sample: 1924)")

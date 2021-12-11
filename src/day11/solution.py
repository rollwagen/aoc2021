octopus_matrix = []
octopus_matrix = [
    [int(value) for value in line.strip()] for line in open("input").readlines()
]
before_any_steps = """11111
19991
19191
19991
11111
'''
octopus_matrix = [
    [int(value) for value in line.strip()]
    for line in before_any_steps.strip().split("\n")
]
"""
octopus_matrix_columns = len(octopus_matrix[0])
octopus_matrix_rows = len(octopus_matrix)

total_flashes = 0


def _flash(flash_row: int, flash_col: int):
    """
    When an octopus flashes, the energy level of all adjacent octopuses is +1,
    incl. octopuses that are diagonally adjacent.
    If this then causes an octopus' energy level to be >9, it also flashes.
    Flashed octopuses are be 'marked' with -1.
    """

    global total_flashes
    total_flashes += 1

    # mark current octopus as flashed
    octopus_matrix[flash_row][flash_col] = -1
    # energy level of all adjacent octopuses by 1, inclduing diagonals
    for mov_row in [-1, 0, 1]:
        for mov_col in [-1, 0, 1]:
            row = flash_row + mov_row
            col = flash_col + mov_col
            if (
                0 <= row < octopus_matrix_rows
                and 0 <= col < octopus_matrix_columns
                and octopus_matrix[row][col] != -1
            ):
                octopus_matrix[row][col] += 1
                if octopus_matrix[row][col] > 9:
                    _flash(row, col)


def _matrix_to_string(matrix: list) -> str:
    return "\n".join(["".join([str(item) for item in row]) for row in matrix])


def part_one(steps: int = 10, until_all_flashed: bool = False) -> int:  # noqa: C901
    if until_all_flashed:  # overwrite number_of_steps to 'inf'
        steps = 1000000000

    for step in range(steps):
        # in each step, energy level of each octopus increases by 1
        for row in range(octopus_matrix_rows):
            for col in range(octopus_matrix_columns):
                octopus_matrix[row][col] += 1

        # any octopus with an energy level greater than 9 flashes
        for row in range(octopus_matrix_rows):
            for col in range(octopus_matrix_columns):
                if octopus_matrix[row][col] > 9:
                    _flash(row, col)

        # any octopus that flashed in a step has its energy level set to 0
        all_flashed = True
        for row in range(octopus_matrix_rows):
            for col in range(octopus_matrix_columns):
                if octopus_matrix[row][col] == -1:
                    octopus_matrix[row][col] = 0
                else:
                    all_flashed = False

        if until_all_flashed and all_flashed:
            return 100 + step + 1  # already did 100 steps in part_one()

    return total_flashes


def part_two() -> int:
    return part_one(until_all_flashed=True)


if __name__ == "__main__":
    print(f"{part_one(100)=}  1649 (sample: 1656)")
    print(f"{part_two()=}  256 (sample: 195)")

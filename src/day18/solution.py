import ast


def addition(number1, number2):
    """
    - form a pair from the left and right parameters
    - apply reduce to that pair
    """
    pair = [number1, number2]
    return reduce(pair)


def reduce(number):
    """
    Note: epeatedly do the first action
    (1) If any pair is nested inside four pairs, the leftmost such pair explodes.
    (2) If any regular number is >= 10, the leftmost such regular number splits.
    """

    # explode()

    # split()


def explode(number):
    pass


def split(number):
    """
    - split a regular number, replace it with a pair
    - left: number divided by two and rounded down
    - right: regular number divided by two and rounded
    [ very (!) inspired by https://github.com/jonathanpaulson/AdventOfCode/ ]
    """
    if isinstance(number, list):

        split_happened, new_number1 = split(number[0])  # 0 = leftmost
        if split_happened:
            return True, [new_number1, number[1]]  # 1 = right part
        else:
            split_happened, new_number2 = split(number[1])  # no split left,go to right
            return split_happened, [new_number1, new_number2]

    elif isinstance(number, int):

        if number >= 10:
            return True, [number // 2, (number + 1) // 2]
        else:
            return False, number


input_ = []
data = [line.strip() for line in open("input.sample").readlines()]
for line in data:
    input_.append(ast.literal_eval(line))

start = input_[0]
for number in input_[1:2]:
    addition(start, number)

# print(magnitude(start))

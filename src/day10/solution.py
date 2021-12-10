from collections import deque
from typing import Deque

input = [line.strip() for line in open("input").readlines()]


class IncompleteError(SyntaxError):
    """Exception raised for incomplete lines."""


class CorruptedError(SyntaxError):
    """Exception raised for corrupted lines.
    Attributes:
     illegal_char -- the illegal char that caused the error
     message -- explanation of the error
    """

    def __init__(self, illegal_char, message):
        self.illegal_char = illegal_char
        self.message = message


matching_chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}

syntax_error_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def parse_line(line: str) -> None:
    stack: Deque = deque()
    for i, char in enumerate(line):
        if i == 0 and char not in matching_chunks.keys():
            raise CorruptedError(char, f"'{char}' is not a valid opening character")
        if char in matching_chunks.keys():  # opening char/bracket
            expected_closing_char = matching_chunks[char]
            stack.append(expected_closing_char)
        elif char in matching_chunks.values():  # closing char/bracket
            expected_closing_char = stack.pop()
            if char != expected_closing_char:
                raise CorruptedError(
                    char,
                    f"Expected '{expected_closing_char}' but found '{char}' instead.",
                )

        if i == len(line) - 1 and stack:
            raise IncompleteError(f"Missing '{stack.pop()}'")


def part_one() -> int:
    total_syntax_error_score = 0
    for line in input:
        try:
            parse_line(line)
        except CorruptedError as e:
            total_syntax_error_score += syntax_error_points[e.illegal_char]
        except IncompleteError:
            continue  # ignore incomplete lines
    return total_syntax_error_score


def part_two() -> int:
    """ """
    return 0


if __name__ == "__main__":
    print(f"{part_one()=} 318081 (sample: 26397)")
    print(f"{part_two()=} (sample: )")

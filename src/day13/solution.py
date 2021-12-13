import pathlib
import re

# from typing import NamedTuple


def parse(input_: str):
    dots_input, fold_input = input_.strip().split("\n\n")
    dots = [tuple(map(int, dot.split(","))) for dot in dots_input.split("\n")]
    # fold along y=7\nfold along x=5
    regex = re.compile(r"fold\ along\ ([a-z])=(\d+)")
    for line in fold_input.splitlines()[:2]:
        axis, value = regex.match(line).groups()  # type: ignore
        if axis == "y":
            fold_y: int = int(value)
        else:
            fold_x: int = int(value)
    print(fold_x, fold_y)
    return dots, (fold_x, fold_y)


def _print_paper(dots: list):
    x_width = max([d[0] for d in dots])
    y_height = max([d[1] for d in dots])
    for y in range(y_height + 1):
        print("".join(["#" if (x, y) in dots else "." for x in range(x_width + 1)]))


def part_one(data) -> int:
    """
    How many dots are visible after completing **just the first**
    fold instruction on your transparent paper?
    """

    dots, folds = data

    # fold vertically i.e. "x"
    x_fold = folds[0]
    new_dots = []
    for dot in dots:
        x, y = dot
        if x < x_fold:
            new_dots.append((x_fold - (x - x_fold), y))
        else:
            new_dots.append((x, y))

    print(f"after first fold {len(set(new_dots))=}")
    return len(set(new_dots))

    dots = new_dots

    # fold horizontally i.e. "y"
    y_fold = folds[1]
    new_dots = []
    for dot in dots:
        x, y = dot
        if y > y_fold:
            new_dots.append((x, y_fold - abs(y - y_fold)))
        else:
            new_dots.append((x, y))

    print(f"after second fold {len(set(new_dots))=}")


def part_two(data) -> int:
    return 0


if __name__ == "__main__":
    print("--- Day 13: Transparent Origami ---")
    input_ = pathlib.Path("input").read_text().strip()
    data = parse(input_)
    print(f"{part_one(data)=}  answer: 785 (sample: 17)")
    print(f"{part_two(data)=}  answer  (sample: )")

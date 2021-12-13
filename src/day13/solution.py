import pathlib
import re


def parse(input_: str):
    dots_input, fold_input = input_.strip().split("\n\n")
    dots = [tuple(map(int, dot.split(","))) for dot in dots_input.split("\n")]
    # fold along y=7\nfold along x=5
    folds = []
    regex = re.compile(r"fold\ along\ ([a-z])=(\d+)")
    for line in fold_input.splitlines():
        axis, value = regex.match(line).groups()  # type: ignore
        if axis == "y":
            folds.append(("y", int(value)))
        else:
            folds.append(("x", int(value)))

    return dots, folds


def _print_paper(dots: list):
    x_width = max([d[0] for d in dots])
    y_height = max([d[1] for d in dots])
    for y in range(y_height + 1):
        BLOCK = chr(0x2588)
        print("".join([BLOCK if (x, y) in dots else "." for x in range(x_width + 1)]))


def part_one(data) -> int:
    dots, folds = data

    first_fold = folds[0]
    fold_direction, fold_value = first_fold
    print(f"{first_fold=}")

    if fold_direction == "x":  # fold vertically i.e. "x"
        new_dots = []
        for dot in dots:
            x, y = dot
            if x > fold_value:
                new_dots.append((fold_value - (x - fold_value), y))
            else:
                new_dots.append((x, y))

    elif fold_direction == "y":  # fold vertically i.e. "y"

        new_dots = []
        for dot in dots:
            x, y = dot
            if y > fold_value:
                new_dots.append((x, fold_value - abs(y - fold_value)))
            else:
                new_dots.append((x, y))

    dots_after_first_fold = len(set(new_dots))
    return dots_after_first_fold


def part_two(data) -> int:
    dots, folds = data

    for fold in folds:
        fold_direction, fold_value = fold

        if fold_direction == "x":  # fold vertically i.e. "x"
            new_dots = []
            for dot in dots:
                x, y = dot
                if x > fold_value:
                    folded_dot = (fold_value - (x - fold_value), y)
                    # print(f'x-> {x=} {y=} {folded_dot=}')
                    new_dots.append(folded_dot)
                else:
                    new_dots.append((x, y))

        elif fold_direction == "y":  # fold vertically i.e. "y"
            new_dots = []
            for dot in dots:
                x, y = dot
                if y > fold_value:
                    new_dots.append((x, fold_value - abs(y - fold_value)))
                else:
                    new_dots.append((x, y))

        dots = new_dots

    _print_paper(dots)
    return len(set(dots))


if __name__ == "__main__":
    print("--- Day 13: Transparent Origami ---")
    input_ = pathlib.Path("input").read_text().strip()
    data = parse(input_)
    print(f"{part_one(data)=}  answer: 785 (sample: 17)")
    print(f"{part_two(data)=}  answer: FJAHJGAH  (sample: -)")

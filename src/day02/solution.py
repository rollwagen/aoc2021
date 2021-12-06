from typing import NamedTuple


class Command(NamedTuple):
    direction: str  # forward, down, up
    unit: int

    @classmethod
    def from_string(cls, string):
        direction, unit = string.split(" ")
        return cls(direction, int(unit))


input = [Command.from_string(line) for line in open("input").readlines()]


def part_one():
    horizontal_position = 0
    depth = 0

    for command in input:
        if command.direction == "forward":
            horizontal_position += command.unit
        elif command.direction == "down":
            depth += command.unit
        elif command.direction == "up":
            depth -= command.unit

    return horizontal_position * depth


def part_two():
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in input:
        if command.direction == "forward":
            horizontal_position += command.unit
            depth += command.unit * aim  # increase depth by aim * X
        elif command.direction == "down":
            aim += command.unit  # increases your aim by units.
        elif command.direction == "up":
            aim -= command.unit  # decreases your aim by units

    return horizontal_position * depth


if __name__ == "__main__":
    print(f"{part_one()=} (2036120)")
    print(f"{part_two()=} (2015547716)")

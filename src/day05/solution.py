import re
from collections import defaultdict
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    start: Point
    end: Point

    @classmethod
    def from_tuple(cls, coords: tuple):
        start = Point(int(coords[0]), int(coords[1]))
        end = Point(int(coords[2]), int(coords[3]))
        return cls(start, end)


# input format per line: "0,9 -> 5,9"
regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
line_segments = [
    Line.from_tuple(regex.match(line.strip()).groups())  # type: ignore
    for line in open("input").readlines()
]
assert len(line_segments) == 500


def _count_point_occurrence(include_diagonal: bool = False) -> defaultdict:
    point_counter: defaultdict = defaultdict(int)
    for line in line_segments:
        if line.start.x == line.end.x:  # vertical line
            y_min = min(line.start.y, line.end.y)
            y_max = max(line.start.y, line.end.y)
            for y in range(y_min, y_max + 1):  # add all line point, incl start+end
                point_counter[(Point(line.start.x, y))] += 1

        elif line.start.y == line.end.y:  # horizontal line
            x_min = min(line.start.x, line.end.x)
            x_max = max(line.start.x, line.end.x)
            for x in range(x_min, x_max + 1):  # add all line point, incl start+end
                point_counter[(Point(x, line.start.y))] += 1

        else:
            if include_diagonal:
                x_direction = 1 if line.start.x < line.end.x else -1
                y_direction = 1 if line.start.y < line.end.y else -1
                x_point_range = range(
                    line.start.x, line.end.x + x_direction, x_direction
                )
                y_point_range = range(
                    line.start.y, line.end.y + y_direction, y_direction
                )
                for x, y in zip(x_point_range, y_point_range):
                    point_counter[(Point(x, y))] += 1

    return point_counter


def part_one() -> int:
    """
    Return the number of points where at least two lines overlap,
    only horizontal and vertical lines.
    """
    point_counter = _count_point_occurrence(include_diagonal=False)
    return sum(True for overlap in point_counter.values() if overlap >= 2)


def part_two() -> int:
    """
    Return the number of points where at least two lines overlap,
    also consider diagonal lines.
    """
    point_counter = _count_point_occurrence(include_diagonal=True)
    return sum(True for overlap in point_counter.values() if overlap >= 2)


if __name__ == "__main__":
    print(f"{part_one()=}   5306 (sample: 5)")
    print(f"{part_two()=}  17787 (sample: 12")

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
    Line.from_tuple(regex.match(line.strip()).groups())
    for line in open("input").readlines()
]
assert len(line_segments) == 500


def part_one() -> int:
    """
    Return the number of points where at least two lines overlap
    """
    point_counter = defaultdict(int)
    for line in line_segments:
        if line.start.x == line.end.x:  # vertical line
            y_min = min(line.start.y, line.end.y)
            y_max = max(line.start.y, line.end.y)
            for y in range(y_min, y_max + 1):  # add all line point, incl start+end
                point_counter[(Point(line.start.x, y))] += 1

        if line.start.y == line.end.y:  # horizontal line
            x_min = min(line.start.x, line.end.x)
            x_max = max(line.start.x, line.end.x)
            for x in range(x_min, x_max + 1):  # add all line point, incl start+end
                point_counter[(Point(x, line.start.y))] += 1

    return sum(True for overlap in point_counter.values() if overlap >= 2)


def part_two() -> int:
    pass


if __name__ == "__main__":
    print(f"{part_one()=}   (sample: 5)")
    print(f"{part_two()=}  ")

input = [line.strip() for line in open("input").readlines()]

"""
x  -->
y  2199943210
   3987894921
|  9856789892
v  ...
   ...
"""
grid = {}
for y, line in enumerate(input):
    for x, value in enumerate(line):
        grid[(x, y)] = int(value)


def part_one() -> int:
    """
    Find the low points - the locations that are lower than any of its adjacent
    locations. Most locations have four adjacent locations (up, left, right, and
    down); locations on the edge or corner of the map have three or two adjacent
    locations, respectively. The risk level of a low point is 1 plus its height.
    """
    neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # above, left, right, below

    def _get_neighbour_values(x: int, y: int) -> list:
        return [grid.get((x + dx, y + dy), float("inf")) for dx, dy in neighbors]

    risk_level_sum = 0
    for point, height in grid.items():
        if grid[point] < min(_get_neighbour_values(*point)):
            risk_level_sum += height + 1

    return risk_level_sum


def part_two() -> int:
    """ """
    return 0


if __name__ == "__main__":
    print("--- Day 9: Smoke Basin ---")
    print(f"{part_one()=}  594 (sample: [1, 0, 5, 5], 15)")
    print(f"{part_two()=}  (sample: )")

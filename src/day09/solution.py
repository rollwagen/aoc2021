from collections import deque

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


def part_one_and_two():

    neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # above, left, right, below

    def _get_neighbour_values(x: int, y: int) -> list:
        return [grid.get((x + dx, y + dy), float("inf")) for dx, dy in neighbors]

    low_points = []
    risk_level_sum = 0
    for point, height in grid.items():
        if grid[point] < min(_get_neighbour_values(*point)):
            low_points.append(point)
            risk_level_sum += height + 1

    print(f"Part One: {risk_level_sum=}")  # ---------------------------------

    def _get_neighbour_points(x: int, y: int) -> list:
        return [(x + dx, y + dy) for dx, dy in neighbors]

    basins = []

    for low_point in low_points:

        queue = deque()
        queue.append(low_point)

        visited = []
        visited.append(low_point)

        basin_values = []
        basin_values.append(grid.get(low_point))  # basin size includes low point

        while queue:
            point = queue.pop()
            for adjacent_point in _get_neighbour_points(*point):
                value_adjacent_point = grid.get(adjacent_point, None)
                if (
                    value_adjacent_point is None
                    or value_adjacent_point == 9
                    or adjacent_point in visited
                ):
                    pass
                else:
                    basin_values.append(value_adjacent_point)
                    visited.append(adjacent_point)
                    queue.append(adjacent_point)

        basins.append(basin_values)

    # three largest basins and multiply their sizes together
    basins.sort(key=len, reverse=True)
    basin_sum = len(basins[0]) * len(basins[1]) * len(basins[2])
    print(f"Part Two: {basin_sum}  858494 (sample: 1134)")


if __name__ == "__main__":
    print("--- Day 9: Smoke Basin ---")
    part_one_and_two()

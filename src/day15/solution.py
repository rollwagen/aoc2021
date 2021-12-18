from collections import defaultdict
from typing import List, Set

data: dict = {}
X_MAX, Y_MAX = 0, 0


def parse(input_: List[str]):
    """
    1163751742
    1381373672
    2136511328
    """
    global data, X_MAX, Y_MAX

    X_MAX = len(input_[0].strip())
    Y_MAX = len(input_)
    print(f"X_MAX: {X_MAX} Y_MAX: {Y_MAX}")

    data = {}
    for y, line in enumerate(input_):
        for x, value in enumerate(line):
            data[(x, y)] = int(value)

    # print(f"data: {data}")

    def _get_neighbor_coords(x: int, y: int) -> list:
        # neighbors are one to the left, right, up, down
        x_y_adjusts = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [coord for coord in x_y_adjusts if coord in data]

    graph: dict = defaultdict(lambda: defaultdict(int))
    for y, line in enumerate(input_):
        for x, value in enumerate(line):
            for (x_neighbour, y_neighbour) in _get_neighbor_coords(x, y):
                graph[(x, y)][(x_neighbour, y_neighbour)] = data[
                    (x_neighbour, y_neighbour)
                ]

    return graph


def _get_lowest_risk_node(risks, processed):
    lowest_risk = float("inf")
    lowest_risk_node = None
    for node in risks.keys():
        if node in processed:
            continue
        risk = risks[node]
        if risk < lowest_risk:
            lowest_risk = risk
            lowest_risk_node = node
    return lowest_risk_node


def part_one(graph) -> int:
    """What is the lowest total risk of
    any path from the top left to the bottom right?"""

    processed: Set[tuple] = set()  # visited nodes ('caves')
    risks = {node: float("inf") for node in data.keys()}  # risk/'cost' to reach node
    risks[(0, 0)] = 0  # start at (0, 0)
    # print(f"risks: {risks}")

    node = _get_lowest_risk_node(risks, processed)

    while node is not None:
        processed.add(node)
        # go through all neighbors
        for neighbor in graph[node].items():
            neighbor_coord, neighbor_risk = neighbor
            old_risk = risks[neighbor_coord]
            new_risk = risks[node] + neighbor_risk
            if new_risk < old_risk:
                risks[neighbor_coord] = new_risk
        node = _get_lowest_risk_node(risks, processed)

    return int(risks[(X_MAX - 1, Y_MAX - 1)])


def part_two(enlarged_graph) -> int:
    return part_one(enlarged_graph)


def enlarge_five_times(original_input):
    _, orig_height = len(original_input[0].strip()), len(original_input)

    enlarged_input = []

    def _adjusted_risk_level(risk_level: str, n: int):
        risk = int(risk_level)
        return str((risk + n - 1) % 9 + 1)  # '9' is the max risk level

    for i, line in enumerate(original_input):
        new_line = ""
        for step in range(0, 5):
            if step == 0:
                new_line += line
                continue
            for risk_level in line:
                new_line += _adjusted_risk_level(risk_level, step)

        enlarged_input.append(new_line)

    for step in range(1, 5):
        for i in range(orig_height):
            new_line = "".join(
                [
                    _adjusted_risk_level(risk_level, step)
                    for risk_level in enlarged_input[i]
                ]
            )
            enlarged_input.append(new_line)

    return enlarged_input


if __name__ == "__main__":
    print("--- Day 15: Chiton ---")
    _input = [line.strip() for line in open("input").readlines()]
    graph = parse(_input)
    print(f"{part_one(graph)=}  answer:748 (sample: 40)")
    graph = parse(enlarge_five_times(_input))
    print(f"{part_two(graph)=}  answer: 3045  (sample: 315)")

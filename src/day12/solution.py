import pathlib
import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e9))


def parse(input: str):
    cave_connections = defaultdict(list)
    for line in input.split("\n"):
        cave1, cave2 = line.strip().split("-")
        cave_connections[cave1].append(cave2)
        cave_connections[cave2].append(cave1)

    return cave_connections


def part_one(cave_connections) -> int:
    visited_lowercase_caves = set()  # visit small caves at most once
    arrived_at_end = []

    def traverse(cave: str) -> int:
        if cave == "end":
            return True  # path to end found
        visited_lowercase_caves.add(cave) if cave.islower() else None
        for destination_cave in cave_connections[cave]:
            if destination_cave not in visited_lowercase_caves:
                if traverse(destination_cave):
                    arrived_at_end.append(1)
        visited_lowercase_caves.remove(cave) if cave.islower() else None
        return False  # path to end not found

    traverse("start")
    return len(arrived_at_end)


def part_two(cave_connections) -> int:
    def traverse(cave: str, visited, cave_visited_twice: bool = False) -> int:
        if cave == "end":
            return 1  # path to end found
        paths = 0
        for destination_cave in cave_connections[cave]:
            if destination_cave.islower():
                if destination_cave not in visited:
                    paths += traverse(
                        destination_cave,
                        visited | {destination_cave},
                        cave_visited_twice,
                    )
                elif not cave_visited_twice and destination_cave not in {
                    "start",
                    "end",
                }:
                    # destination_cave has been visited once already, hence now 'True'
                    paths += traverse(
                        destination_cave, visited | {destination_cave}, True
                    )
                elif cave_visited_twice and destination_cave in visited:
                    pass  # can only visit a _single_ small cave twice
            else:  # destination_cave is uppercase
                paths += traverse(destination_cave, visited, cave_visited_twice)
        return paths

    return traverse("start", {"start"}, False)


if __name__ == "__main__":
    print("--- Day 12: Passage Pathing ---")
    input = pathlib.Path("input").read_text().strip()
    data = parse(input)
    print(f"{part_one(data)=}  answer: 3738 (sample: 10)")
    print(f"{part_two(data)=}  answer 120506 (sample: 36)")

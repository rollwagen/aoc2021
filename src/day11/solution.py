octopus_matrix = []
octopus_matrix = [
    [int(value) for value in line.strip()] for line in open("input.sample").readlines()
]
before_any_steps = """11111
19991
19191
19991
11111
"""
octopus_matrix = [
    [int(value) for value in line.strip()]
    for line in before_any_steps.strip().split("\n")
]
print(f"{octopus_matrix=}")


def part_one() -> int:
    return 0


def part_two() -> int:
    return 0


if __name__ == "__main__":
    print(f"{part_one()=}  (sample: )")
    print(f"{part_two()=}  (sample: )")

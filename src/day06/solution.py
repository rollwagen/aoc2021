# sample input: 3,4,3,1,2
input = [int(days) for days in open("input").read().split(",")]
# input=[3, 4, 3, 1, 2]
fish_counter = [input.count(i) for i in range(0, 9)]
# fish_count=[0, 1, 1, 2, 1, 0, 0, 0, 0]


def part_one(days: int = 80) -> int:
    """ """
    for _ in range(0, days):
        counter_zero_reproducers = fish_counter.pop(0)
        # each day, a 0 becomes a 6 (7 days) and
        # adds a new 8 (9 days) to the end of the list
        fish_counter.append(counter_zero_reproducers)
        fish_counter[6] += counter_zero_reproducers
    return sum(fish_counter)


def part_two() -> int:
    remaining_days_to_calculate = 256 - 80
    return part_one(remaining_days_to_calculate)


if __name__ == "__main__":
    print(f"{part_one()=}  379414 (sample: 18=26, 80=5934)")
    print(f"{part_two()=}  1705008653296 (sample: 256=26984457539)")

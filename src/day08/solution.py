input = [line.strip() for line in open("input").readlines()]


segments_to_digit = {
    2: 1,  # used two segments (c and f)
    4: 4,  # uses four segments
    3: 7,  # uses three segments
    7: 8,  # uses all seven segments
}


def part_one() -> int:
    appearances = 0
    for entry in input:
        signal_patterns, output_values = (part.strip() for part in entry.split("|"))
        for value in output_values.split():
            if segments_to_digit.get(len(value)) is not None:
                appearances += 1

    return appearances


def part_two() -> int:
    """ """
    return 0


if __name__ == "__main__":
    print(f"{part_one()=} 543 (sample: 26)")
    print(f"{part_two()=}  (sample: )")


measurements = [int(line.strip()) for line in open("input").readlines()]


def part_one():
    depth = float('inf')
    number_of_increases = 0
    for next_depth in measurements:
        if next_depth > depth:
            number_of_increases = number_of_increases + 1
        depth = next_depth
    print(f'Part One: {number_of_increases=}')


def part_two():
    number_of_increases = 0
    i: int = 0
    previous_three_sum = float('inf')
    while i <= len(measurements)-3:  # three measurements
        three_sum = sum(measurements[i:i+3])
        if three_sum > previous_three_sum:
            number_of_increases = number_of_increases + 1
        previous_three_sum = three_sum
        i = i + 1

    print(f'Part Two: {number_of_increases=}')


if __name__ == '__main__':
    part_one()
    part_two()

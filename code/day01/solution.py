
measurements = [int(line.strip()) for line in open("input").readlines()]


def part_one():
    depth = float('inf')
    number_of_increases = 0
    for next_depth in measurements:
        if next_depth > depth:
            number_of_increases += 1
        depth = next_depth

    # same as a one liner:
    nm = sum(m2 > m1 for m1, m2 in zip(measurements, measurements[1:]))

    print(f'Part One: {number_of_increases=} {nm=}')


def part_two():
    number_of_increases = 0
    previous_three_sum = float('inf')
    for i in range(0, len(measurements)-2):
        three_sum = sum(measurements[i:i+3])
        if three_sum > previous_three_sum:
            number_of_increases += 1
        previous_three_sum = three_sum

    # more elegant would be to leverage:
    # a + b + c < b + c + d _if_ a < d

    print(f'Part Two: {number_of_increases=}')


if __name__ == '__main__':
    part_one()  # 1548
    part_two()  # 1589

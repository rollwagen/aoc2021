
input = [line.strip() for line in open("input").readlines()]

BINARY_INPUT_LENGTH = len(input[0])


def part_one() -> int:
    binary_number_bit_count = [0] * BINARY_INPUT_LENGTH

    input_length = len(input)
    print(f'{input_length=}')

    for line in input:
        bytes_list = list(line)
        for i in range(BINARY_INPUT_LENGTH):
            binary_number_bit_count[i] += int(bytes_list[i])
    print(f'{binary_number_bit_count=}')

    binary_most_common = [0] * BINARY_INPUT_LENGTH
    binary_least_common = [0] * BINARY_INPUT_LENGTH

    for i in range(BINARY_INPUT_LENGTH):
        if binary_number_bit_count[i] > input_length/2:
            binary_most_common[i] = 1
        else:
            binary_most_common[i] = 0

    binary_least_common = [0 if bit == 1 else 1 for bit in binary_most_common]

    gamma = int("".join([str(b) for b in binary_most_common]), 2)
    epsilon = int("".join(str(b) for b in binary_least_common), 2)

    return gamma * epsilon


if __name__ == '__main__':
    print(f'{part_one()=}')

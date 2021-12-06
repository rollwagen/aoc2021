from typing import List

input = [line.strip() for line in open("input").readlines()]

BINARY_INPUT_LENGTH = len(input[0])


def _calculate_most_and_least_common_bits(input: List[str]):
    INPUT_LENGTH = len(input)

    binary_number_bit_count = [0] * BINARY_INPUT_LENGTH

    for line in input:
        bytes_list = list(line)
        for i in range(BINARY_INPUT_LENGTH):
            binary_number_bit_count[i] += int(bytes_list[i])
    # print(f'{binary_number_bit_count=}')

    binary_most_common = [0] * BINARY_INPUT_LENGTH
    binary_least_common = [0] * BINARY_INPUT_LENGTH

    for i in range(BINARY_INPUT_LENGTH):
        if binary_number_bit_count[i] >= INPUT_LENGTH / 2:
            binary_most_common[i] = 1
        else:
            binary_most_common[i] = 0

    binary_least_common = [0 if bit == 1 else 1 for bit in binary_most_common]

    return (binary_most_common, binary_least_common)


def part_one_and_two():

    binary_most_common, binary_least_common = _calculate_most_and_least_common_bits(
        input
    )

    print(f"{binary_most_common=}")

    gamma = int("".join([str(b) for b in binary_most_common]), 2)
    epsilon = int("".join(str(b) for b in binary_least_common), 2)

    print(f"part_one = {gamma * epsilon}  (775304)")

    def _filter_rating(index: int, oxy_gen_list, bit_criteria_most=True) -> list:
        # print(f'_filter.... {index=}')
        oxy_most_common, oxy_least_common = _calculate_most_and_least_common_bits(
            oxy_gen_list
        )
        # print(f'{oxy_most_common=}')
        if bit_criteria_most is True:
            new_list = [
                item
                for item in oxy_gen_list
                if int(item[index]) == oxy_most_common[index]
            ]
        else:
            new_list = [
                item
                for item in oxy_gen_list
                if int(item[index]) == oxy_least_common[index]
            ]
        # print(f'{new_list=}')
        return new_list

    oxygen_generator = input
    for i in range(BINARY_INPUT_LENGTH):
        oxygen_generator = _filter_rating(i, oxygen_generator)
    print(f"{oxygen_generator=}")

    co2_scrubber = input
    for i in range(BINARY_INPUT_LENGTH):
        co2_scrubber = _filter_rating(i, co2_scrubber, False)
        if len(co2_scrubber) == 1:
            break
    print(f"{co2_scrubber=}")

    print(
        f"part_two={int(oxygen_generator[0], 2) * int(co2_scrubber[0], 2)} (1370737)"  # noqa: E501
    )


if __name__ == "__main__":
    part_one_and_two()

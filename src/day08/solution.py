from collections import defaultdict

input = [line.strip() for line in open("input").readlines()]
# input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
# input = [line.strip() for line in open("input.sample").readlines()]


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
    sum_output_values = 0

    for entry in input:

        signal_numbers = defaultdict(list)  # 5: ['cdfbe', 'gcdfa'], 3: ['dab']
        signal_pattern_mapping = {digit: None for digit in range(0, 10)}

        entry_signal_patterns, entry_output_values = (
            part.strip() for part in entry.split("|")
        )
        for signal in entry_signal_patterns.split():
            signal_length = len(signal)
            signal_numbers[signal_length].append(signal)

            # record mappings for digits 1, 4, 7, and 8
            # because they use a unique number of segments
            digit = segments_to_digit.get(signal_length)
            if digit is not None:
                signal_pattern_mapping[digit] = set(signal)

        # determine digit '6' amongst the three six segment
        # digits '0', '6' and '9'
        # - digit '6' only has one out of c + f
        # - digit '9' has both c + f
        # - digit '0' has both c + f
        for six_segment in signal_numbers[6]:
            if len(signal_pattern_mapping[1] - set(six_segment)) == 1:
                signal_pattern_mapping[6] = set(six_segment)  # digit '6'

        # ...similar for digits using five segments
        # - digit '2' only has one out of c + f
        # - digit '5' only has one out of c + f
        # - digit '3' uses both c + f
        for five_segment in signal_numbers[5]:
            if len(signal_pattern_mapping[1] - set(five_segment)) == 0:
                signal_pattern_mapping[3] = set(five_segment)  # digit '3'
            elif len(set(five_segment) - signal_pattern_mapping[6]) == 1:
                signal_pattern_mapping[2] = set(five_segment)  # digit '2'
            elif len(set(five_segment) - signal_pattern_mapping[6]) == 0:
                signal_pattern_mapping[5] = set(five_segment)  # digit '5'

        for six_segment in signal_numbers[6]:
            if set(six_segment) in signal_pattern_mapping.values():
                continue  # digit '6' already determined above

            if len(signal_pattern_mapping[5] - set(six_segment)) == 0:
                signal_pattern_mapping[9] = set(six_segment)  # digit '9'
            else:
                signal_pattern_mapping[0] = set(six_segment)  # digit '0'

        output_number = ""
        _, output_values = (part.strip() for part in entry.split("|"))
        for value in output_values.split():
            for digit, mapping_value in signal_pattern_mapping.items():
                if set(value) == mapping_value:
                    output_number += str(digit)

        sum_output_values += int(output_number)

    return sum_output_values


if __name__ == "__main__":
    print(f"{part_one()=} 543 (sample: 26)")
    print(f"{part_two()=} 994266 (sample: 61229, single example: 5353)")

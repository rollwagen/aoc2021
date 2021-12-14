import pathlib
import typing
from collections import Counter


def parse(input_: str):
    template_input, rule_input = input_.split("\n\n")
    rules = {}
    for rule in rule_input.split("\n"):
        rule_from, rule_to = rule.split(" -> ")[0], rule.split(" -> ")[1]
        rules[rule_from] = rule_to
    pairs: typing.Counter = Counter(
        template_input[i : i + 2] for i in range(len(template_input) - 1)  # noqa: E203
    )

    return pairs, rules


def part_one(data, steps: int = 10) -> int:
    pairs, rules = data
    for step in range(1, steps + 1):
        _pairs: typing.Counter = Counter()
        for (left, right), count in pairs.items():
            middle = rules[left + right]

            _pairs[left + middle] += count
            _pairs[middle + right] += count

        pairs = _pairs

        counter: typing.Counter = Counter()
        for pair, count in pairs.items():
            element = pair[0]
            counter[element] += count

        last_initial_polymer_element = list(data[0])[-1][1]
        counter[last_initial_polymer_element] += 1

        elements: typing.Counter = Counter()
        for (left, right), n in pairs.items():
            elements[left] += n
        elements[last_initial_polymer_element] += 1

    return max(elements.values()) - min(elements.values())


def part_two(data) -> int:
    return part_one(data, steps=40)


if __name__ == "__main__":
    print("--- Day 14: Extended Polymerization ---")
    input_ = pathlib.Path("input").read_text().strip()
    data = parse(input_)
    print(f"{part_one(data)=}  answer: 3118 (sample: 1588)")
    print(f"{part_two(data)=}  answer: 4332887448171  (sample: 2188189693529)")

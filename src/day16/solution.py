import pathlib
from collections import deque


class Packet:
    def __init__(self, version, type_id):
        # header: These two values are numbers
        # most significant bit first i.e. 100 = number 4
        self.version: int  # first three bits encode the packet version
        self.type_id: int  # next three bits encode the packet type ID

    # Packets with type ID 4 represent a literal value.
    #   groups of four bits. Each group is prefixed by a 1
    #   except last prefixed by a 0 bit
    #   hese groups of five bits immediately follow the packet header (see above)


def parse(input_: str):
    bits_transmission = bin(int(input_, 16))[2:]
    # print(f'{bits_transmission=}')
    return deque(bits_transmission)


def _read_int(n: int):
    """Read n bits and return converted to int."""
    return int("".join([data.popleft() for _ in range(n)]), 2)


def part_one(data) -> int:
    version = _read_int(3)
    type_id = _read_int(3)
    print(f"{version=} {type_id=}")
    if type_id == 4:
        # while ..read one bit == 1, read another four block
        pass

    return 0


def part_two(data) -> int:
    return 0


if __name__ == "__main__":
    print("--- Day 16: Packet Decoder ---")
    input_ = pathlib.Path("input").read_text().strip()
    data = parse(input_)
    print(f"{part_one(data)=}  answer: (sample: )")
    # print(f"{part_two(data)=}  answer  (sample: )")

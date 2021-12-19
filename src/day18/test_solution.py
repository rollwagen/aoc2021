import pathlib

import pytest  # type: ignore
import solution as s

DIR = pathlib.Path(__file__).parent


def test_split():
    assert s.split(10) == (True, [5, 5])
    assert s.split(11) == (True, [5, 6])
    assert s.split(12) == (True, [6, 6])
    assert s.split([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]) == (
        True,
        [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
    )
    assert s.split([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]) == (
        True,
        [
            [[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
            [1, 1],
        ],
    )


@pytest.fixture
def sample_input():
    input_ = [line.strip() for line in open((DIR / "input.sample")).readlines()]
    return s.parse(input_)


@pytest.fixture
def puzzle_input():
    input_ = [line.strip() for line in open((DIR / "input")).readlines()]
    return s.parse(input_)


@pytest.mark.skip
def test_parse_sample(sample_input):
    """Test that input is parsed properly"""
    assert len(sample_input) == 100


@pytest.mark.skip
def test_part_one_sample(sample_input):
    assert s.part_one(sample_input) == 40


@pytest.mark.skip
def test_part_one_puzzle(puzzle_input):
    assert s.part_one(puzzle_input) == 748


@pytest.mark.skip
def test_part_two_sample(sample_input):
    assert s.part_two(sample_input) == -1


@pytest.mark.skip
def test_part_two_puzzle(puzzle_input):
    assert s.part_two(puzzle_input) == -1

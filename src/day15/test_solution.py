import pathlib

import pytest  # type: ignore
import solution as s

DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample_input():
    input_ = [line.strip() for line in open((DIR / "input.sample")).readlines()]
    return s.parse(input_)


@pytest.fixture
def puzzle_input():
    input_ = [line.strip() for line in open((DIR / "input")).readlines()]
    return s.parse(input_)


def test_parse_sample(sample_input):
    """Test that input is parsed properly"""
    assert len(sample_input) == 100


def test_part_one_sample(sample_input):
    assert s.part_one(sample_input) == 40


def test_part_one_puzzle(puzzle_input):
    assert s.part_one(puzzle_input) == 748


@pytest.mark.skip
def test_part_two_sample(sample_input):
    assert s.part_two(sample_input) == -1


@pytest.mark.skip
def test_part_two_puzzle(puzzle_input):
    assert s.part_two(puzzle_input) == -1

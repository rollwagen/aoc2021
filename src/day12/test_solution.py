import pathlib

import pytest
import solution as s

DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample():
    input = (DIR / "input.sample").read_text().strip()
    return s.parse(input)


@pytest.fixture
def puzzle_input():
    input = (DIR / "input").read_text().strip()
    return s.parse(input)


def test_parse_sample(sample):
    """Test that input is parsed properly"""
    assert len(sample["A"]) == 4


def test_part_one_sample(sample):
    assert s.part_one(sample) == 10


def test_part_one_puzzle_input(puzzle_input):
    assert s.part_one(puzzle_input) == 3738


def test_part_two_sample(sample):
    assert s.part_two(sample) == 36

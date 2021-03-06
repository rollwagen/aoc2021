import pathlib

import pytest  # type: ignore
import solution as s

DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample_input():
    input = (DIR / "input.sample").read_text().strip()
    return s.parse(input)


@pytest.mark.skip(reason="Not implemented")
@pytest.fixture
def puzzle_input():
    input = (DIR / "input").read_text().strip()
    return s.parse(input)


def test_parse_sample(sample_input):
    """Test that input is parsed properly"""
    assert 0 == 1


def test_part_one_sample(sample_input):
    """After the first fold in sample, 17 dots are visible."""
    assert s.part_one(sample_input) == 17
    paper_after_folding = """\
            #####
            #...#
            #...#
            #...#
            #####
            .....
            .....
    """
    print(paper_after_folding)


@pytest.mark.skip(reason="Not implemented")
def test_part_one_puzzle(puzzle_input):
    assert s.part_one(puzzle_input) == -1


@pytest.mark.skip(reason="Not implemented")
def test_part_two_sample(sample_input):
    assert s.part_two(sample_input) == -1


@pytest.mark.skip(reason="Not implemented")
def test_part_two_puzzle(puzzle_input):
    assert s.part_two(puzzle_input) == -1

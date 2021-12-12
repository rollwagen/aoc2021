import pathlib

import pytest
import solution as s

DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample():
    input = (DIR / "input.sample").read_text().strip()
    return s.parse(input)


def test_parse_sample(sample):
    """Test that input is parsed properly"""
    assert len(sample["A"]) == 3

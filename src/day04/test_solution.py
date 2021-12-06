import unittest

from solution import part_one, part_two


class Day04Test(unittest.TestCase):
    def test_part_one(self):
        # for sample input https://adventofcode.com/2021/day/4
        self.assertEqual(32844, part_one())

    def test_part_two(self):
        self.assertEqual(4920, part_two())

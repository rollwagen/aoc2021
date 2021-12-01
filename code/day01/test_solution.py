import unittest

from solution import part_one, part_two


class Day01Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1548, part_one())

    def test_part_two(self):
        self.assertEqual(1589, part_two())

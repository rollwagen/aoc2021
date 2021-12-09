import unittest

from solution import part_one, part_two


class Day09Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(594, part_one())

    def test_part_two(self):
        self.assertEqual(-1, part_two())

import unittest

from solution import part_one, part_two


class Day05Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(5306, part_one())

    def test_part_two(self):
        self.assertEqual(17787, part_two())

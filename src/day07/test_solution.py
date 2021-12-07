import unittest

from solution import part_one, part_two


class Day07Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(335330, part_one())

    def test_part_two(self):
        self.assertEqual(92439766, part_two())

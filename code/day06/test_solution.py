import unittest

from solution import part_one, part_two


class Day06Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(379414, part_one())

    def test_part_two(self):
        self.assertEqual(1705008653296, part_two())

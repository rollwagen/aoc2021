import unittest

from solution import CorruptedError, IncompleteError, parse_line


class Day10Test(unittest.TestCase):
    def test_parse_line_opening_with_closing_bracket(self):
        # Opens with a closing bracket
        corrupted_line = ">([(<{}[<>[]}>{[]{[(<()>"
        self.assertRaises(CorruptedError, parse_line, corrupted_line)

    def test_parse_line_corrupted01(self):
        # Expected ], but found } instead
        corrupted_line = "{([(<{}[<>[]}>{[]{[(<()>"
        self.assertRaises(CorruptedError, parse_line, corrupted_line)

    def test_parse_line_corrupted02(self):
        # Expected ], but found ) instead.
        corrupted_line = "[[<[([]))<([[{}[[()]]]"
        self.assertRaises(CorruptedError, parse_line, corrupted_line)

    def test_parse_line_incomplete(self):
        incomplete_line = "[({(<(())[]>[[{[]{<()<>>"
        self.assertRaises(IncompleteError, parse_line, incomplete_line)

    """
    Further Corrupted examples:
    [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
    [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
    <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
    """

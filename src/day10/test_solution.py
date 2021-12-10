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

    def test_parse_line_incomplete01(self):
        #  Complete by adding }}]])})].
        incomplete_line = "[({(<(())[]>[[{[]{<()<>>"
        with self.assertRaises(IncompleteError) as error:
            parse_line(incomplete_line)
            self.assertEqual(
                error.missing_closing_chars, ["}", "}", "]", "]", ")", "}", "]"]
            )

    """
    Further Corrupted examples:
    [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
    [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
    <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
    """

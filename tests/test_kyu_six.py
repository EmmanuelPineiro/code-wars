from unittest import TestCase

from src.kyu_six import to_camel_case, duplicate_encode


class TestToCamelCase(TestCase):
    def test_to_camel_case_empty(self):
        result = to_camel_case("")
        expected = ""
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_to_camel_case_snake(self):
        result = to_camel_case("the_stealth_warrior")
        expected = "theStealthWarrior"
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_to_camel_case_dash(self):
        result = to_camel_case("The-Stealth-Warrior")
        expected = "TheStealthWarrior"
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_to_camel_case_screaming_dash(self):
        result = to_camel_case("A-B-C")
        expected = "ABC"
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")


class TestDuplicateEncode(TestCase):
    def test_duplicate_encode_no_dupes(self):
        result = duplicate_encode("din")
        expected = "((("
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_duplicate_encode_some_dupes(self):
        result = duplicate_encode("recode")
        expected = "()()()"
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_duplicate_encode_case_sensitive(self):
        result = duplicate_encode("Success")
        expected = ")())())"
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

    def test_duplicate_encode_special_chars(self):
        result = duplicate_encode("(( @")
        expected = "))(("
        self.assertEqual(result, expected, f"expected: {expected}\nreceived: {result}")

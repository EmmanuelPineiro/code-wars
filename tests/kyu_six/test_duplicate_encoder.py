from src.kyu_six.duplicate_encoder import duplicate_encode


class TestDuplicateEncoder:

    def test_duplicate_encode_no_dupes(self):
        result = duplicate_encode("din")
        expected = "((("
        assert result == expected

    def test_duplicate_encode_some_dupes(self):
        result = duplicate_encode("recode")
        expected = "()()()"
        assert result == expected

    def test_duplicate_encode_case_sensitive(self):
        result = duplicate_encode("Success")
        expected = ")())())"
        assert result == expected

    def test_duplicate_encode_special_chars(self):
        result = duplicate_encode("(( @")
        expected = "))(("
        assert result == expected

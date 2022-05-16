from src.kyu_six.convert_string_to_camel_case import to_camel_case


class TestToCamelCase:

    def test_to_camel_case_empty(self):
        result = to_camel_case("")
        expected = ""
        assert result == expected

    def test_to_camel_case_snake(self):
        result = to_camel_case("the_stealth_warrior")
        expected = "theStealthWarrior"
        assert result == expected

    def test_to_camel_case_dash(self):
        result = to_camel_case("The-Stealth-Warrior")
        expected = "TheStealthWarrior"
        assert result == expected

    def test_to_camel_case_screaming_dash(self):
        result = to_camel_case("A-B-C")
        expected = "ABC"
        assert result == expected

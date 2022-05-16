import re


def to_camel_case(text):
    """
    https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

    Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first
    word within the output should be capitalized only if the original word was capitalized (known as Upper Camel
    Case, also often referred to as Pascal case). Examples

    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


    :param text: the text to convert to camel case
    :return: the text as camel case
    """
    result = ''
    if text:
        words = re.split("[-_]", text)

        for word in words:
            if result:
                result += word[:1].upper() + word[1:]
            else:
                result += word

    return result


def duplicate_encode(word):
    """
    https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

    The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
    that character appears only once in the original string, or ")" if that character appears more than once in the
    original string. Ignore capitalization when determining if a character is a duplicate.

    Examples

    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))(("

    Notes

    Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode
    XXX", the "XXX" is the expected result, not the input!

    :param word:
    :return:
    """
    # your code here

    return "((("

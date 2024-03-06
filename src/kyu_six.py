import re


def to_camel_case(text):
    """
    https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

    Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first
    word within the output should be capitalized only if the original word was capitalized (known as Upper Camel
    Case, also ofasdfasdf
        words = re.split("[-_]", text)

        for word in words:
          asdf
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

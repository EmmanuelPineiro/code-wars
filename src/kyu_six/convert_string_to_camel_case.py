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

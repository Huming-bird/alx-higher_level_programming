#!/usr/bin/python3

def text_indentation(text):
    """ This function prints a text with 2 new lines after
    each of the specified characters.

    Args:
    text: must be a string data type.

    Output:
    line indented texts
    """

    for letter in text:
        if letter in (".", "?", ":"):
            print(letter, "\n\n", end='')
        else:
            print(letter, end='')

#!/usr/bin/env python3
"""Kentucky Friar"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print("".join(map(fry, re.split(r"(\W+)", line.rstrip()))))


# --------------------------------------------------
def fry(word):
    """Drop the `g` from `-ing` words, change `you` to `y'all`"""

    if word.lower() == "you":
        return word[0] + "'all"

    if word.endswith("ing"):
        if any(map(lambda c: c.lower() in "aeiouy", word[:-3])):
            return word[:-1] + "'"

    return word


# --------------------------------------------------
def test_fry():
    """Test fry"""

    assert fry("you") == "y'all"
    assert fry("You") == "Y'all"
    assert fry("your") == "your"
    assert fry("fishing") == "fishin'"
    assert fry("Aching") == "Achin'"
    assert fry("swing") == "swing"


# --------------------------------------------------
if __name__ == "__main__":
    main()

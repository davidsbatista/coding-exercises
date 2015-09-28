__author__ = 'dsbatista'

"""
- Find out whether an array/string contains non-repeated characters.
"""


def has_repeated(s):
    words = set()
    for x in s:
        if x not in words:
            words.add(x)
        else:
            return True
    return False


def main():
    s = "sem igual"
    print has_repeated(s)


if __name__ == "__main__":
    main()
__author__ = 'dsbatista'

"""
- uppercase all the words in string which have length of 3
"""


def uppercase(s):
    new_string = ''
    for x in s.split():
        if len(x) == 3:
            new_string += ' '+x.upper()
        else:
            new_string += ' '+x
    return new_string

def main():
    s = "ist isto eh uma palavra sim"
    print uppercase(s)


if __name__ == "__main__":
    main()
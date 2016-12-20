#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
- AAABCDDDE
- A3BCD3E
"""

# TODO: use a multiset or a hashtable to store the frequency of each char


def main():

    input_string = "AAABCDDDE"
    input_string = "AAABCC"
    compressed = ''
    count = 0

    print input_string
    print len(input_string), range(len(input_string))

    for i in range(len(input_string)):
        if i+2 > len(input_string):
            if count == 0:
                compressed += input_string[i]
            break

        if input_string[i] != input_string[i+1]:
            """
            if input_string[i+1] != input_string[i+2]:
                compressed += input_string[i]
            else:
            """
            count += 1
            compressed += input_string[i] + str(count)
            count = 0
        else:
            count += 1

    print compressed

if __name__ == "__main__":
    main()



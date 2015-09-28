#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
- For a given array count combination of pairs of (x,y) whose sum is N.
"""


def find_pairs(arr_, k):
    values = dict()
    for x in arr_:
        if x in values:
            print x, values[x]
        else:
            values[k-x] = x


def main():
    find_pairs([2, 3, 5, 7, 4, 1, 8, 0, 3], 5)

if __name__ == "__main__":
    main()
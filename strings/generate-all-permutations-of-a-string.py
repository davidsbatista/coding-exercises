#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
- Generate a list of all permutation of a string
"""


def permute(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                res += [c + perm]
    return res


def main():
    s = "ABC"
    for x in (enumerate(s)):
        print x
    for permutation in permute(s):
        print permutation

if __name__ == "__main__":
    main()

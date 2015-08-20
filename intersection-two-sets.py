#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"


# You have two sets. How can you find the intersection?

# put contents of the first set into hashtable and
# iterate over second set, checking if hashtable contains current element.
# O(n)

def intersect(arr_a, arr_b):

    result = dict()
    common = []

    for i in arr_a:
        result[i] = 0

    for z in arr_b:
        if z in result:
            common.append(z)

    return common


def main():
    x_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    b_array = [-2, 1, -3, 4, 0, 2, 1, -5, 4]
    print intersect(x_array, b_array)


if __name__ == "__main__":
    main()
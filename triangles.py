#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
For example, if the input array is {4, 6, 3, 7}, the output should be 3.
There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.
As another example, consider the array {10, 21, 22, 100, 101, 200, 300}.
There can be 6 possible triangles: {10, 21, 22}, {21, 100, 101}, {22, 100, 101}, {10, 100, 101},
{100, 101, 200} and {101, 200, 300}
"""

points = set()


def triangle(a, b, c):
    if a+b > c and b+c > a and a+c > b:
        return True
    else:
        return False


def triangles(arra_a):
    for a in range(0, len(arra_a), 1):
        for b in range(1, len(arra_a), 1):
            for c in range(2, len(arra_a), 1):
                #if a != b and b != c and a != c:
                    if triangle(arra_a[a], arra_a[b], arra_a[c])is True:
                        #TODO: discard repetead, i.e., tuples with different order of elements
                        points.add((arra_a[a], arra_a[b], arra_a[c]))

    return points


def main():
    x_array = [10, 21, 22, 100, 101, 200, 300]
    result = triangles(x_array)
    for t in result:
        print t
    print len(result)


if __name__ == "__main__":
    main()
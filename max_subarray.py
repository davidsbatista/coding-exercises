#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
In computer science, the maximum subarray problem is the task of finding the contiguous subarray within a
one-dimensional array of numbers (containing at least one positive number) which has the largest sum.
For example, for the sequence of values −2, 1, −3, 4, −1, 2, 1, −5, 4; the contiguous subarray with the
largest sum is 4, −1, 2, 1, with sum 6.
"""


def max_subarray(arr):
    max_so_far = 0
    max_ending_here = 0

    for x in arr:
        max_ending_here = max_ending_here + x

        if max_ending_here < 0:
            max_ending_here = 0

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


def main():
    x_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print max_subarray(x_array)

if __name__ == "__main__":
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
In computer science, the maximum subarray problem is the task of finding the contiguous subarray within a
one-dimensional array of numbers (containing at least one positive number) which has the largest sum.
For example, for the sequence of values −2, 1, −3, 4, −1, 2, 1, −5, 4; the contiguous subarray with the
largest sum is 4, −1, 2, 1, with sum 6.
{2,-1, 3,-5,3} output: 4
"""


def max_sum_subarray(arr):
    max_so_far = 0
    max_ending_here = 0

    for i, x in enumerate(arr):
        max_ending_here = max_ending_here + x

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        elif max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


# find the largest subsequence given an array that yields the largest sum.
def maxsumseq(arr):
    max_so_far = 0
    max_ending_here = 0
    start, end, sum_start = -1, -1, -1

    for i, x in enumerate(arr):
        max_ending_here = max_ending_here + x

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start, end = sum_start, i

        elif max_ending_here < 0:
            max_ending_here = 0
            sum_start = i

    return max_so_far, start, end, arr[start + 1:end + 1]

#TODO: Find the largest subsequence of the given array that yields the largest PRODUCT.
#TODO: Maximum product subset with negative and positive integers


def main():
    x_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print max_sum_subarray(x_array)
    print maxsumseq(x_array)

if __name__ == "__main__":
    main()
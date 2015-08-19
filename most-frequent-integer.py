#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"


# Find the most frequent integer in an array, x_array

def most_frequent(x_array):

    counts = dict()

    for i in x_array:
        try:
            print counts
            counts[i] += 1
        except Exception:
            counts[i] = 0

    print counts
    print counts.values()
    print max(counts, key=counts.get)


def main():
    x_array = [2,2,2,2,2,2,2,234,23,534,2,1,23,4,34,4,2,123,2,32]
    most_frequent(x_array)

if __name__ == "__main__":
    main()
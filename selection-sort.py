import sys

__author__ = 'dsbatista'

"""
The algorithm divides the input list into two parts: 
    the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and 
    the sublist of items remaining to be sorted that occupy the rest of the list. 
    
    Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
    The algorithm proceeds by 
        finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
        exchanging it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
"""


def selection_sort(arr_n):
    
    sorted_sublist = []
    size = len(arr_n)
    
    while len(sorted_sublist) != size:
        # find the minimum element
        min_ = sys.maxint            # maximum possible integer
        min_index = -1
        for i, x in enumerate(arr_n):
            if x < min_:
                min_ = x
                min_index = i

        # exchange it with the leftmost unsorted element
        sorted_sublist.append(min_)
        del arr_n[min_index]

    return sorted_sublist


def main():
    x_array = [2, 2, 2, 2, 2, 2, 2, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    print selection_sort(x_array)

if __name__ == "__main__":
    main()
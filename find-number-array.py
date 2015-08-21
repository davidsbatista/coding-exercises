__author__ = 'dsbatista'

"""
- Given a sorted array with duplicates and a number, find the range in the form of (startIndex, endIndex) of that number.
For example:

find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1).

The array and the number of duplicates can be large.
"""


#TODO: use a binary search tree
def find_number(arr, n):
    start = -1
    end = -1
    found = False
    
    for x in range(0, len(arr)):
        if found is True and arr[x] == n:
            continue
        
        if found is True and arr[x] != n:
            end = x
            break
                   
        if arr[x] == n and found is False:
            start = x
            found = True
        
    return start,end
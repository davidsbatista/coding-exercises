__author__ = 'dsbatista'

"""
The algorithm divides the input list into two parts: 

    A function called Insert designed to insert a value into a sorted sequence at the beginning of an array.
    It operates by beginning at the end of the sequence and shifting each element one place to the right until a
    suitable position is found for the new element. The function has the side effect of overwriting the value stored
    immediately after the sorted sequence in the array.
    
    - To perform an insertion sort, begin at the left-most element of the array and invoke Insert to insert each
    element encountered into its correct position.
    - The ordered sequence into which the element is inserted is stored at the beginning of the array in the set of
    indices already examined. Each insertion overwrites a single value: the value being inserted.
"""


"""
def insert(sorted_array, new_value):
    print "\nnew value", new_value
    print "array", sorted_array
    for i in range(len(sorted_array)-1, -1, -1):
        if new_value > sorted_array[i]:
            # shift i+1, inclusive, everything to the right, and insert 'new_value'
            print "sorted", sorted_array[:i+1] + [new_value] + sorted_array[i+1:]
            return sorted_array[:i+1] + [new_value] + sorted_array[i+1:]
    if i == 0:
        # insert value at the begining of the sorted array
        print "sorted", [new_value] + sorted_array
        return [new_value] + sorted_array


def insertion_sort(arr_n):
    for i in range(1, len(arr_n)):
        arr_n = insert(arr_n[:i] + arr_n[i+1:], arr_n[i])
    return arr_n
"""

#TODO: https://en.wikipedia.org/wiki/Insertion_sort


def insertion_sort(arr_a):
    for i in range(1, len(arr_a)):
        x = arr_a[i]
        j = i
        while j > 0 and arr_a[j-1] > x:
            arr_a[j] = arr_a[j-1]
            j -= 1
        arr_a[j] = x
    return arr_a


def main():
    x_array = [2, 2, 2, 2, 2, 2, 2, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    print insertion_sort(x_array)

if __name__ == "__main__":
    main()
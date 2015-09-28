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
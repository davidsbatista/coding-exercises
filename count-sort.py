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


def count_sort(arr_a, k):
    arr_b = [0 for _ in arr_a]
    arr_c = [0 for _ in range(0, k)]

    print "A", arr_a
    print "B", arr_b
    print "C", arr_c

    # in position i of arr_c the number of elements equal to i (i.e., in arr_a)
    for i in range(0, len(arr_a)):
        arr_c[arr_a[i]-1] += 1

    print "C", arr_c

    # store in c how many elements are less than or equal to i
    for i in range(1, k):
        arr_c[i] += arr_c[i - 1]

    print "C", arr_c

    for i in range(len(arr_a)-1, -1, -1):
        arr_b[arr_c[arr_a[i]-1]-1] = arr_a[i]
        arr_c[arr_a[i]-1] -= 1
        print "B", arr_b
        print "C", arr_c

    return arr_b


def main():
    #x_array = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 8, 10]
    x_array = [3, 6, 4, 1, 3, 4, 1, 4]
    k = max(x_array)
    print count_sort(x_array, k)

if __name__ == "__main__":
    main()

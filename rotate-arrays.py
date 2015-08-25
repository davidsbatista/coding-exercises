__author__ = 'dsbatista'


"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
-> 1,2,3,4,5,6,7
-> rotate by 2
-> 3,4,5,6,7,1,2
"""


def rotate(arr, d):
    temp = []
    for i in range(d, len(arr)):
        temp.append(arr[i])
    for i in range(0, d):
        temp.append(arr[i])

    return temp


def is_rotated(arr_a, arr_b):

    # check if same size



def main():
    x_array = [1, 2, 3, 4, 5, 6, 7]
    print rotate(x_array, 2)

    # Find an element in a rotated array.
    # http://stackoverflow.com/questions/4773807/searching-in-an-sorted-and-rotated-array

    # Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array.
    # Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}

if __name__ == "__main__":
    main()
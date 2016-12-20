__author__ = 'dsbatista'

"""
- Pick an element, called a pivot, from the array.

- Reorder the array so that all elements with values less than the pivot come
before the pivot, while all elements with values greater than the pivot come
after it (equal values can go either way). After this partitioning, the pivot
is in its final position. This is called the partition operation.

- Recursively apply the above steps to the sub-array of elements with smaller
values and separately to the sub-array of elements with greater values.
"""


def partition(my_list, start, end):
    pivot = my_list[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and my_list[left] <= pivot:
            left += 1
        while my_list[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            # swap places
            temp = my_list[left]
            my_list[left] = my_list[right]
            my_list[right] = temp

    # swap start with myList[right]
    temp = my_list[start]
    my_list[start] = my_list[right]
    my_list[right] = temp
    return right


def quicksort(my_list, start, end):
    if start < end:
        # partition the list
        pivot = partition(my_list, start, end)
        # sort both halves
        quicksort(my_list, start, pivot-1)
        quicksort(my_list, pivot+1, end)
    return my_list


def main():
    x_array = [2, 3, 22, 27, 21, 20, 28, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    print quicksort(x_array, 0, len(x_array)-1)


if __name__ == "__main__":
    main()
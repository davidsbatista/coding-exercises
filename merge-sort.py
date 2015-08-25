__author__ = 'dsbatista'


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(my_list):
    if len(my_list) < 2:
        return my_list
    middle = len(my_list) / 2
    left = mergesort(my_list[:middle])
    right = mergesort(my_list[middle:])
    return merge(left, right)


def main():
    x_array = [2, 3, 22, 27, 21, 20, 28, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    print mergesort(x_array)


if __name__ == "__main__":
    main()
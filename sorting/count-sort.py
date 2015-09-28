__author__ = 'dsbatista'


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
    x_array = [2, 2, 2, 2, 2, 2, 2, 234, 23, 534, 2, 1, 23, 4, 34, 4, 2, 123, 2, 32]
    k = max(x_array)
    print count_sort(x_array, k)

if __name__ == "__main__":
    main()

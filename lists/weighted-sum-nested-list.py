"""
Given a nested list of integers, return the sum of all integers in the list
weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)
"""


def depth_sum(list_int, depth):
    print "new call", list_int

    if not list_int or len(list_int) == 0:
        return 0
    if isinstance(list_int[0], int):
        return list_int[0] * depth + depth_sum(list_int[1:], depth)

    elif isinstance(list_int[0], list):
        print list_int
        print list_int[0]
        print list_int[1:]
        return sum(list_int[0], depth+1) + depth_sum(list_int[1:], depth)


def main():
    """
    array_1 = [1, 1, 1]             # 3
    array_2 = [[1, 1], 2, [1, 1]]   # 4 + 2 + 4 = 10
    array_3 = [2, [2], 2]           # 2 + 4 + 2 = 8
    """
    array_4 = [2, [2, [2]], 2]      # 2 + 4 + 6 + 2 = 14
    """
    weighted_sum = depth_sum(array_1, 1)
    print array_1, weighted_sum

    weighted_sum = depth_sum(array_2, 1)
    print array_2, weighted_sum

    weighted_sum = depth_sum(array_3, 1)
    print array_3, weighted_sum
    """

    weighted_sum = depth_sum(array_4, 1)
    print array_4, weighted_sum


if __name__ == '__main__':
    main()

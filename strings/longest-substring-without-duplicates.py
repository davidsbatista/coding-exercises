"""
Given a string, please get the length of the longest substring which does not
have duplicated characters. Supposing all characters in the string are in
the range from 'a' to 'z'.
"""


def find_longest_non_duplicate(input_string):

    longest = 0
    max_longest = 0

    for i in range(len(input_string)):
        if i+1 > len(input_string)-1:
            return max_longest

        if input_string[i] == input_string[i+1] and longest != 0:
            if longest > max_longest:
                max_longest = longest
            longest = 0
        else:
            longest += 1


def main():
    max_lenght = find_longest_non_duplicate("abcdddeef")
    print "abcdddeef", max_lenght

    max_lenght = find_longest_non_duplicate("abcdddeef")
    print "abcdddeef", max_lenght


if __name__ == '__main__':
    main()

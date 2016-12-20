__author__ = 'dsbatista'

"""
Testing a sequence of characters to determine if it is a palindrome
(i.e., reads the same forward and backward, like "radar") can be accomplished
easily with one stack and one queue.

The solution is to enter the sequence of characters into both data structures,
then remove letters from each data structure one at a time and compare them,
making sure that the letters match.
"""


def is_palindrom(word):

    my_stack = []  # (FIFO)
    my_queue = []  # (LIFO)

    for w in word:
        my_stack.append(w)
        my_queue.append(w)

    while len(my_queue) > 0 and len(my_stack) > 0:

        # remove from queue
        x = my_queue[0]
        del my_queue[0]

        # remove from stack
        y = my_stack.pop()

        # as long as the two words are the same continue comparing
        if x == y:
            continue
        else:
            print word, "is not a plaindrome"
            return None

    print word, "is a plaindrome"


def main():
    is_palindrom("radar")
    is_palindrom("gone")

if __name__ == "__main__":
    main()


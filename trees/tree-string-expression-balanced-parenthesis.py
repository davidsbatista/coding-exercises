
from collections import defaultdict

"""
Given a tree string expression in balanced parenthesis format:

(A(B(C)(D))(E)(F))

               A
             / | \
            B  E  F
           / \
          C   D

The function is to return the root of the tree you build, and if you can please
print the tree with indentations like above.

You can print in the simplified format.
        A
    B   E  F
   C  D
"""


def parse_string(s):
    levels = defaultdict(list)  # dict of lists
    level_count = 0
    for i, c in enumerate(s):
        if c == '(':
            level_count += 1
        elif c == ')':
            level_count -= 1
        else:
            levels[level_count].append(c)
    return levels


def print_levels(levels):
    for level in levels:
        for c in levels[level]:
            print c,
        print


def main():
    #tree = "(A(B(C))"
    #tree = "(A(B(C)D)"
    tree = "(A(B(C)(D))(E)(F))"
    levels = parse_string(tree)
    # TODO make sure that levels are accesed in order
    # sort the dict into a list
    print_levels(levels)

if __name__ == "__main__":
    main()

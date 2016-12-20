#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
- Given two strings, determine if they are isomorphic.

Two words are called isomorphic if the letters in one word can be remapped to
get the second word. Remapping a letter means replacing all occurrences of it
with another letter while the ordering of the letters remains unchanged.
No two letters may map to the same letter, but a letter may map to itself.

Example:

given "foo", "app";
True: we can map 'f->'a' and 'o'->'p'

given "foo", "boa";
False: we can map 'f'- 'b', 'o'->'o', we can't map 'o'->'a'

* * given "bar", "foo";
False: we can't map both 'a' and 'r' to 'o'

given "turtle", "tletur";
True: we can map 't'->'t', 'u'->'l', 'r'->'e', 'l'->'u', 'e'->'r'

given "ab", "ca";
True: we can map 'a'->'c', 'b'->'a'
"""


def isomorphism(str1, str2):
        a = dict()
        b = dict()

        for i in str1:
            a[i] = str1.count(i)

        for j in str2:
            b[j] = str2.count(j)

        if sorted(a.values()) == sorted(b.values()):
            return True
        else:
            return False


def main():
    str1 = "turtle"
    str2 = "tletur"
    print isomorphism(str1, str2)

    str1 = "foo"
    str2 = "app"
    print isomorphism(str1, str2)

if __name__ == "__main__":
    main()
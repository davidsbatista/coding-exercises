#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

"""
- two words is Isomorphic ?
- Given two words as Strings, determine if they are isomorphic.

Two words are called isomorphic if the letters in one word can be remapped to get the second word.
Remapping a letter means replacing all occurrences of it with another letter while the ordering of the
letters remains unchanged. No two letters may map to the same letter, but a letter may map to itself.

Example: * given "foo", "app";
returns true * we can map 'f->'a' and 'o'->'p'

given "foo", "boa";
returns false * we can map 'f' -&gt; 'b', 'o' -&gt; 'o', we can't map 'o' -&gt; 'a'

* * given "bar", "foo";
returns false * we can't map both 'a' and 'r' to 'o'

given "turtle", "tletur";
returns true * we can map 't' -&gt; 't', 'u' -&gt; 'l', 'r' -&gt; 'e', 'l' -&gt; 'u', 'e' -&gt;'r'

given "ab", "ca";
returns true * we can map 'a' -&gt; 'c', 'b' -&gt; 'a'
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

if __name__ == "__main__":
    main()
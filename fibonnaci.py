#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

__author__ = "David S. Batista"
__email__ = "dsbatista@inesc-id.pt"

cache = [0] * 10000


def fibonnaci(x):

    if x == 0:
        return 0

    if x == 1:
        return 1

    if cache[x] != 0:
        return cache[x]     # return cached result

    cache[x] = (fibonnaci(x-1) + fibonnaci(x-2))    # cache result

    return fibonnaci(x)


def main():
    #print len(cache)
    #print cache
    x = int(sys.argv[1])
    fibonnaci(x)
    print "Fib("+str(x)+")"
    print cache[:x]

if __name__ == "__main__":
    main()
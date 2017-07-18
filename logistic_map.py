#!/usr/bin/python
#coding=utf8

import sys

script, x, r, nIter = sys.argv
x = float(x)
r = float(r)
nIter = int(nIter)

def nextX(x, r):
    return 1.0 * r * x * (1 - x)

for i in range(nIter):
    x = nextX(x, r)
    print x

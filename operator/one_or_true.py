#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/10


def test_one():
    arr = [i if 1 else False for i in range(1000)]
    return arr


def test_true():
    arr = [i if True else False for i in range(1000)]
    return arr

if __name__ == '__main__':
    """
    It seems influenced by something other
    """
    import timeit
    # 489.2671+ 42.8531+ 42 44.31+
    print("one", "\t", timeit.timeit("test_one()", setup="from __main__ import test_one"))
    # 502.0336+ 45.8043+ 41.52+
    print("true", "\t", timeit.timeit("test_true()", setup="from __main__ import test_true"))

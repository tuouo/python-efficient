#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/4/10


def test_generation():
    arr = [True if i & 1 else False for i in range(1000)]
    return arr


def test_generation1():
    arr = [True if i % 2 else False for i in range(1000)]
    return arr


def test_generation2():
    arr = [True if i % 2 == 1 else False for i in range(1000)]
    return arr

if __name__ == '__main__':
    import timeit
    print("& ", "\t", timeit.timeit("test_generation()", setup="from __main__ import test_generation"))  # 154.4950+
    print("//", "\t", timeit.timeit("test_generation1()", setup="from __main__ import test_generation1"))  # 121.6736+
    print("==", "\t", timeit.timeit("test_generation2()", setup="from __main__ import test_generation2"))  # 155.6789+

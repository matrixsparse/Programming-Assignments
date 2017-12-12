# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


class InsertSort(object):
    """
    插入排序
    """

    def __init__(self):
        pass

    def swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t


if __name__ == "__main__":
    arr = [20, 14, 77, 58, 65, 84, 75, 22, 62, 54, 11]
    i = InsertSort()
    i.sort(arr)
    print(arr)

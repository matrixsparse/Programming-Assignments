# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


class SelectionSort(object):
    """
    选择排序
    """

    def __init__(self):
        pass

    def sort(self, arr):
        for i in range(0, len(arr)):
            minIndex = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            self.swap(arr, i, minIndex)

    def swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t


if __name__ == "__main__":
    arr = [20, 14, 77, 58, 65, 84, 75, 22, 62, 54, 11]
    i = SelectionSort()
    i.sort(arr)
    print(arr)

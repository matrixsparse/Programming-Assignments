package com.matrix.algorithms;

/**
 * 插入排序
 *
 * 插入排序当中有两个循环，假设数组的大小为n，
 * 则第一个循环是n－1次，第二个while循环在最坏的情况下是1到n－1次。因此插入排序的时间复杂度大约为如下形式
 * 1+2+3+4+...＋n－1 ＝ n（n－1）/ 2 ＝ O（n2）
 */
public class InsertSort {

    // 算法类不允许产生任何实例
    private InsertSort() {
    }

    private static void sort(int arr[]) {

        // 找到每轮中最小的元素
        for (int i = 1; i < arr.length; i++) {
            // 寻找元素arr[i]合适的插入位置
            for (int j = i; j > 0 && arr[j] < arr[j - 1]; j--) {
                swap(arr, j, j - 1);
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        int[] arr = {20, 14, 77, 58, 65, 84, 75, 22, 62, 54, 11};
        InsertSort.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
    }
}

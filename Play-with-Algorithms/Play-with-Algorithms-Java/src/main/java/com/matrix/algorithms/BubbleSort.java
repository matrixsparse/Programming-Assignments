package com.matrix.algorithms;

/**
 * 冒泡排序
 */
public class BubbleSort {

    // 算法类不允许产生任何实例
    private BubbleSort() {
    }

    private static void sort(int arr[]) {
        // 找到每轮中最小的元素
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        int[] arr = {20, 14, 77, 54, 65, 84, 75, 22, 65, 54, 11};
        BubbleSort.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
    }
}

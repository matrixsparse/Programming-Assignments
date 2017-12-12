package com.matrix.algorithms;

/**
 * 快速排序
 * 1.选定一个合适的值（理想情况中值最好，但实现中一般使用数组第一个值）,称为"枢轴"(pivot)
 * 2.基于这个值，将数组分为两部分，较小的分在左边，较大的分在右边
 * 3.可以肯定，如此一轮下来，这个枢轴的位置一定在最终位置上
 * 4.对两个子数组分别重复上述过程，直到每个数组只有一个元素
 * 5.排序完成
 */
public class QuickSort {


    // 我们的算法类不允许产生任何实例
    private QuickSort() {
    }

    // 对arr[l...r]部分进行partition操作
    // 返回p, 使得arr[l...p-1] < arr[p] ; arr[p+1...r] > arr[p]
    private static int partition(int[] arr, int l, int r) {

        int v = arr[l];

        int j = l; // arr[l+1...j] < v ; arr[j+1...i) > v
        for (int i = l + 1; i <= r; i++)
            if (arr[i] < v) {
                j++;
                swap(arr, j, i);
            }

        swap(arr, l, j);

        return j;
    }

    // 递归使用快速排序,对arr[l...r]的范围进行排序
    private static void sort(int[] arr, int l, int r) {

        if (l >= r)
            return;

        int p = partition(arr, l, r);
        sort(arr, l, p - 1);
        sort(arr, p + 1, r);
    }

    public static void sort(int[] arr) {

        int n = arr.length;
        sort(arr, 0, n - 1);
    }

    private static void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        int[] arr = {20, 14, 77, 58, 65, 84, 75, 22, 62, 54, 11};
        QuickSort.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
    }
}

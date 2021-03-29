package com.matrix.designpattern.factory;

/**
 * 这种单例模式(内部类的方式来实现)，是我们实际开发过程中最常用的
 */
public class InnerClassFullSingletonPatternDemo {

    public static void main(String[] args) {

    }

    /**
     * 可以做饱汉模式
     *
     * 内部类，只要没有被使用，就不会初始化，Singleton的实例就不会创建
     *
     * 在第一次有人调用getInstance方法的时候，内部类会初始化，创建一个Singleton的实例
     *
     * 然后java能确保的一点是，类静态初始化的过程一定只会执行一次
     */
    public static class Singleton {

        private Singleton() {

        }

        public static class InnerHolder {
            public static final Singleton instance = new Singleton();
        }

        public static Singleton getInstance() {
            return InnerHolder.instance;
        }
    }

}
package com.matrix.designpattern.factory;

/**
 * 享元模式
 */
public class FlyweightPatternDemo {

    public static void main(String[] args) {
        // 享元

        // 享受，元数据
        // 同一个数据，就认为是一个元数据，整个系统里整个数据就一份，缓存起来
        // 整个系统对整个数据，全部享受他一个对象实例即可

        // 直接既有内存来缓存一块数据，用享元模式
    }

    public static interface Flyweight {
        void execute();

        String getName();

        void setName(String name);
    }


}

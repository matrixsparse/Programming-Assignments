package com.matrix.designpattern.factory;

/**
 * 没有使用外观模式的实现
 */
public class WithoutFacadePatternDemo {

    public static void main(String[] args) {
        // 假设我们这里是子系统2，要基于子系统1的3个模块的功能实现一个业务逻辑
        ModuleA modulesA = new ModuleA();
        ModuleB modulesB = new ModuleB();
        ModuleC modulesC = new ModuleC();

        modulesA.execute();
        modulesB.execute();
        modulesC.execute();

        // 这么搞会有什么问题？

        // 问题一：对应子系统1来说，维护成本太高了，就是因为要care多个子系统2的模块。如果只是3个模块还凑合，若是20个模块呢？那子系统1对于子系统2的
        // 各个模块的了解就要很多，维护成本很高

        // 问题二：就是多个模块组成的一个功能，如果在子系统1的多个地方都使用到了，那么那段代码就会在多个地方有重复，复制黏贴的过程，一旦这段业务逻辑修改了
        // 比如还要加入一个模块D的功能，可能就要修改多个地方的代码，会弄得非常麻烦

    }

    public static class ModuleA {
        public void execute() {
            System.out.println("子系统1的模块A的功能");
        }
    }

    public static class ModuleB {
        public void execute() {
            System.out.println("子系统1的模块B的功能");
        }
    }

    public static class ModuleC {
        public void execute() {
            System.out.println("子系统1的模块C的功能");
        }
    }
}

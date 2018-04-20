package com.matrix.designpattern.factory;

/**
 * 模板方法设计模式
 */
public class TemplateMethodPatternDemo {

    public static void main(String[] args) {
        DiscountCalculate1 calculate1 = new DiscountCalculate1();
        calculate1.calculate();

        DiscountCalculate2 calculate2 = new DiscountCalculate2();
        calculate2.calculate();

        DiscountCalculate3 calculate3 = new DiscountCalculate3();
        calculate3.calculate();
    }

    /**
     * 折扣折算接口
     */
    public interface DiscountCalculator {
        void calculate();
    }

    /**
     * 模板方法实现的精华所在
     */
    public static abstract class AbstractDiscountCalculator implements DiscountCalculator {
        public void calculate() {
            // 完成通用计算逻辑
            commonCalculate();
            // 完成特殊计算逻辑
            specifiCalculate();
        }

        private void commonCalculate() {
            System.out.println("通用的计算逻辑，修改了下....");
        }

        protected abstract void specifiCalculate();
    }

    public static class DiscountCalculate1 extends AbstractDiscountCalculator {
        protected void specifiCalculate() {
            System.out.println("完成特殊的计算逻辑1");
        }
    }

    public static class DiscountCalculate2 extends AbstractDiscountCalculator {
        protected void specifiCalculate() {
            System.out.println("完成特殊的计算逻辑2");
        }
    }

    public static class DiscountCalculate3 extends AbstractDiscountCalculator {
        protected void specifiCalculate() {
            System.out.println("完成特殊的计算逻辑3");
        }
    }
}

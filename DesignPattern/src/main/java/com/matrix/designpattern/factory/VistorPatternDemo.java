package com.matrix.designpattern.factory;

import java.util.ArrayList;
import java.util.List;

/**
 * 访问者模式
 */
public class VistorPatternDemo {

    public static void main(String[] args) {

    }

    public static class Department {

        private String name;

        private List<Department> children = new ArrayList<Department>();

        public Department(String name) {
            super();
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName() {
            this.name = name;
        }

        public List<Department> getChildren() {
            return children;
        }

        public void setChildren(List<Department> children) {
            this.children = children;
        }

    }
}


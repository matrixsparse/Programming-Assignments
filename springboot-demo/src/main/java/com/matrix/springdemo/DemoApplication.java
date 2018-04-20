package com.matrix.springdemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 这个注解代表了spring boot中的核心功能，auto configuration
 *
 * 它是说，确认可以启用这个auto configuration这个功能 auto configuration，就是我们后面在spring
 * boot源码剖析的阶段 auto configuration的核心思想，其实就是说，只要我们引入一个starter类的依赖，自动会根据我们引入了什么依赖
 * 然后来判断说，我们要干什么事情，接着说自动给我们完成所有的配置
 *
 * 比如说spring-boot-starter-web，引入了这个依赖 同时我们启动了auto
 * configuration，此时就会根据说，我们引入了starter-web这个依赖，就认为说我们要开发一个web系统 此时就会自动给我们进行auto
 * configuration，完成web系统需要的所有的配置 包括了所有依赖包的引入，spring mvc的配置，web.xml的配置，spring
 * mvc+spring的整合，tomcat的配置
 *
 * @author matrix
 *
 */
@EnableAutoConfiguration
/**
 * 它就是一个Spring mvc的注解
 *
 * @RestController就表明说，这个是一个spring mvc的controller
 * @RestController的意思是说，就仅仅提供RESTful接口，返回结果给浏览器，不会走传统读渲染模板视图页面 我们这里是一个demo，所以说简化了一下，就将spring
 *                                                             mvc的controller和入口类合并到一起了
 *
 * @author matrix
 *
 */
@RestController
/*
 *
 * 梳理一下spring boot启动的一个过程
 *
 * （1）auto configuration完成了所有的配置：spirng mvc、spring、tomcat
 * （2）会将内嵌的tomcat准备好，同时将我们的这个工程部署到内嵌的tomcat中去的
 * （3）接着就会启动内嵌的一个tomcat
 * （4）tomcat启动之后，就会初始化spring的核心容器，是跟spring mvc整合在一起的
 * （5）spring核心容器就会去扫描所有的包，有没有带@RestController之类的注解，如果有，则将这个controller初始化
 * （6）将我们的@RestController注解的类实例化成一个bean，注入自己的spirng容器
 * （7）此时spring mvc的核心servlet，去对外接收请求的，接收到请求之后，就会将请求转发给对应的controller bean
 * （8）controller bean处理完请求之后，spring mvc将请求结果，返回给浏览器
 *
 */
public class DemoApplication {

    @RequestMapping("/hello/{name}")
    public String sayHello(@PathVariable("name") String name) {
        return "hello," + name + ",this is spring boot demo";
    }

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
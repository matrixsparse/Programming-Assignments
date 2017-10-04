# spring-cloud-demo

## 传统架构的问题

* 单块应用，耦合严重
* 开发速度慢，新需求
* 不易于扩展和重构
* 不易于技术升级

## 微服务架构的几大特征：

* 足够单一的职责与功能
* 微型
* 面向服务的思想
* 独立开发：团队，技术选型，前后端分离，存储分离，独立部署
* 自动化开发流程：编码，自动化测试，持续集成，自动化部署

## Spring Boot和微服务

* spring boot不是微服务技术
* spring boot只是一个用于加速开发spring应用的基础框架，简化工作，开发单块应用很适合
* 如果要直接基于spring boot做微服务，相当于需要自己开发很多微服务的基础设施，比如基于zookeeper来实现服务注册和发现
* spring cloud才是微服务技术

## 什么是注册中心

（1）就是首先有一个eureka server，服务的注册与发现的中心
（2）你如果写好了一个服务，就可以将其注册到eureka server上去
（3）然后别人的服务如果要调用你的服务，就可以从eureka server上查找你的服务所在的地址，然后调用

## Eureka基本原理

（1）服务都会注册到eureka的注册表
（2）eureka有心跳机制，自动检测服务，故障时自动从注册表中摘除
（3）每个服务也会缓存euraka的注册表，即使eureka server挂掉，每个服务也可以基于本地注册表缓存，与其他服务进行通信
（4）只不过是如果eureka server挂掉了，那么无法发布新的服务了

### eureka-servser/pom.xml

```bash
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.matrix.eureka</groupId>
    <artifactId>eureka-servser</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.2.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <!--eureka server -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-eureka-server</artifactId>
        </dependency>

        <!-- spring boot test-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Dalston.RC1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
</project>
```

### eureka-servser/resources/application.yml

```bash
server:
  port: 8761

eureka:
  instance:
    hostname: localhost
  client:
    registerWithEureka: false
    fetchRegistry: false
    serviceUrl:
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
```

### eureka-servser/java/EurekaServer.java

```bash
package com.matrix.eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@EnableEurekaServer
@SpringBootApplication
public class EurekaServer {

    public static void main(String[] args) {
        SpringApplication.run(EurekaServer.class,args);
    }
}
```

### eureka-client/pom.xml

```bash
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.matrix.eureka</groupId>
    <artifactId>say-hello-server</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.2.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-eureka</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Dalston.RC1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
</project>
```

### eureka-client/resources/application.yml

```bash
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8761/eureka/
server:
  port: 8762
spring:
  application:
    name: service-say-hello
```

### eureka-client/java/SayHelloApplication.java

```bash
package com.matrix.eureka;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableEurekaClient
@RestController
public class SayHelloApplication {

    public static void main(String[] args) {
        SpringApplication.run(SayHelloApplication.class, args);
    }

    @Value("${server.port}")
    String port;

    @RequestMapping("/sayHello")
    public String home(@RequestParam String name) {
        return "hello，" + name + " from port：" + port;
    }
}
```

## 访问http://localhost:8761/，查看eureka是否启动成功

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk040azchxj22je10w7d1.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk03ia2uc7j22k41dqdpy.jpg)

## 访问http://localhost:8762/sayHello?name=matrix

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk042mc7tdj21i2086gnw.jpg)

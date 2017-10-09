# Spring Cloud之Ribbon+Rest调用负载均衡

## 创建Maven工程greeting-rest

## 导入依赖

>pom.xml

```bash
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
		<groupId>org.springframework.cloud</groupId>
		<artifactId>spring-cloud-starter-ribbon</artifactId>
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
```

>application.yml

```bash
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8761/eureka/
server:
  port: 8764
spring:
  application:
    name: greeting-rest
```

>Application

```bash
package com.matrix.ribbon;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

// @EnableDiscoveryClient，向eureka注册自己作为一个服务的调用client
// 之前的服务，EnableEurekaClient，代表的是向eureka注册自己，将自己作为一个服务
@SpringBootApplication
@EnableDiscoveryClient
public class GreetingRestApplication {

    public static void main(String[] args) {
        SpringApplication.run(GreetingRestApplication.class, args);
    }

    // 在spring容器中注入一个bean，RestTemplate，作为rest服务接口调用的客户端
    // @LoadBalanced标注，代表对服务多个实例调用时开启负载均衡
    @Bean
    @LoadBalanced
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

>调用service-say-hello

```bash
package com.matrix.ribbon.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

// 写一个服务，注入RestTemplate服务调用客户端
@Service
public class GreetingService {

    @Autowired
    private RestTemplate restTemplate;

    // 用SAY-HELLO-SERVICE这个服务名替代实际的ip地址
    // ribbon负载在多个服务实例之间负载均衡，每次调用随机挑选一个实例，然后替换服务名
    public String greeting(String name) {
        return restTemplate.getForObject("http://SERVICE-SAY-HELLO/sayHello?name=" + name, String.class);
    }

}
```

>controller

```bash
package com.matrix.ribbon.controller;

import com.matrix.ribbon.service.GreetingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    @Autowired
    private GreetingService greetingService;

    @RequestMapping(value = "/greeting")
    public String greeting(@RequestParam String name) {
        return greetingService.greeting(name);
    }
}
```

>多次访问http://localhost:8764/greeting?name=matrix，发现每次访问的端口都不一样，在多个服务实例之间负载均衡了


![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkc5bqipqlj20gd046q30.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkc5bqxi1fj20fz04swek.jpg)


## 新建maven项目

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmxn5ir4aj21gy0tytay.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmxn7q7bdj21gy0tyn5x.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmxn8lbpbj21u61aa7bf.jpg)

## 项目结构

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmyuo200vj20ig0o0q58.jpg)

## Auto-import

```bash
Auto-import自动导入依赖
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmxqkraqmj21uy0g6wih.jpg)

## 代码实现

### pom.xml

```bash
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.matrix.hystrix</groupId>
    <artifactId>hystrix-example</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.2.5.RELEASE</version>
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
            <version>1.2.2</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.2.8</version>
        </dependency>
        <dependency>
            <groupId>org.apache.tomcat</groupId>
            <artifactId>tomcat-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.1.43</version>
        </dependency>
    </dependencies>

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
            <id>spring-milestone</id>
            <url>https://repo.spring.io/libs-release</url>
        </repository>
    </repositories>

    <pluginRepositories>
        <pluginRepository>
            <id>spring-milestone</id>
            <url>https://repo.spring.io/libs-release</url>
        </pluginRepository>
    </pluginRepositories>
</project>
```

### src/main/java/**/UserMapper.java

```bash
package com.matrix.hystrix.ha.mapper;

/**
 *
 */
public interface UserMapper {
}
```

### src/main/resources/mybatis/UserMapper.xml

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.matrix.hystrix.ha.mapper.UserMapper">

</mapper>
```

### src/main/resources/templates/hello.html

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
</body>
</html>
```

### src/main/resources/Application.properties 

```bash
server.port=8081
spring.datasource.url=jdbc:mysql://115.28.240.96:3306/hystrix_demo
spring.datasource.username=hystrix_demo
spring.datasource.password=hystrix_demo
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
```

### src/main/java/**/HelloController.java

```bash
package com.matrix.hystrix.ha.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @RequestMapping("/hello")
    @ResponseBody
    public String hello(String name) {
        return "hello，" + name;
    }

}
```

### src/main/java/**/Application.java

```bash
package com.matrix.hystrix.ha;


import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.PlatformTransactionManager;

import javax.sql.DataSource;

/**
 * 启动web应用的入口类
 */
@EnableAutoConfiguration
@SpringBootApplication
@ComponentScan
@MapperScan("com.matrix.hystrix.ha.mapper")
public class Application {

    @Bean
    @ConfigurationProperties(prefix = "spring.datasource")
    public DataSource dataSource() {
        return new org.apache.tomcat.jdbc.pool.DataSource();
    }

    @Bean
    public SqlSessionFactory sqlSessionFactoryBean() throws Exception {
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        sqlSessionFactoryBean.setDataSource(dataSource());
        PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
        sqlSessionFactoryBean.setMapperLocations(resolver.getResources("classpath:/mybatis/*.xml"));
        return sqlSessionFactoryBean.getObject();
    }

    @Bean
    public PlatformTransactionManager transactionManager() {
        return new DataSourceTransactionManager(dataSource());
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}
```

## 运行程序

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmypynkkoj22l21a07wh.jpg)

## 在浏览器查看

```bash
http://localhost:8081/hello?name=matrix
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjmypoxvloj21do0bswgp.jpg)

## 缓存服务

### pom.xml

```bash
<dependency>
	<groupId>org.apache.httpcomponents</groupId>
	<artifactId>httpclient</artifactId>
	<version>4.4</version>
</dependency>
```

### src/main/java/**/HttpClientUtils.java

```bash
package com.matrix.hystrix.ha.http;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

/**
 * HttpClient工具类
 */
@SuppressWarnings("deprecation")
public class HttpClientUtils {
    /**
     * 发送GET请求
     *
     * @param url 请求URL
     * @return 响应结果
     */
    @SuppressWarnings("resource")
    public static String sendGetRequest(String url) {
        String httpResponse = null;

        HttpClient httpclient = null;
        InputStream is = null;
        BufferedReader br = null;

        try {
            // 发送GET请求
            httpclient = new DefaultHttpClient();
            HttpGet httpget = new HttpGet(url);
            HttpResponse response = httpclient.execute(httpget);

            // 处理响应
            HttpEntity entity = response.getEntity();
            if (entity != null) {
                is = entity.getContent();
                br = new BufferedReader(new InputStreamReader(is));

                StringBuffer buffer = new StringBuffer("");
                String line = null;

                while ((line = br.readLine()) != null) {
                    buffer.append(line + "\n");
                }

                httpResponse = buffer.toString();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (br != null) {
                    br.close();
                }
                if (is != null) {
                    is.close();
                }
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }

        return httpResponse;
    }

    /**
     * 发送post请求
     *
     * @param url URL
     * @param map 参数Map
     * @return
     */
    @SuppressWarnings({"rawtypes", "unchecked", "resource"})
    public static String sendPostRequest(String url, Map<String, String> map) {
        HttpClient httpClient = null;
        HttpPost httpPost = null;
        String result = null;

        try {
            httpClient = new DefaultHttpClient();
            httpPost = new HttpPost(url);

            //设置参数
            List<NameValuePair> list = new ArrayList<NameValuePair>();
            Iterator iterator = map.entrySet().iterator();
            while (iterator.hasNext()) {
                Entry<String, String> elem = (Entry<String, String>) iterator.next();
                list.add(new BasicNameValuePair(elem.getKey(), elem.getValue()));
            }
            if (list.size() > 0) {
                UrlEncodedFormEntity entity = new UrlEncodedFormEntity(list, "utf-8");
                httpPost.setEntity(entity);
            }

            HttpResponse response = httpClient.execute(httpPost);
            if (response != null) {
                HttpEntity resEntity = response.getEntity();
                if (resEntity != null) {
                    result = EntityUtils.toString(resEntity, "utf-8");
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {

        }

        return result;
    }
}
```

### src/main/java/**/CacheController.java

```bash
package com.matrix.hystrix.ha.controller;

import com.matrix.hystrix.ha.http.HttpClientUtils;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * 缓存服务的接口
 */
@Controller
public class CacheController {

    @RequestMapping("/change/product")
    @ResponseBody
    public String changeProduct(Long productId) {
        // 拿到一个商品id
        // 调用商品服务的接口，获取商品id对应的商品的最新数据
        // 用HttpClient去调用商品服务的http接口

        // 往http接口发送一条消息，就认为是通知缓存服务，有一个商品的数据变更了
        String url = "http://127.0.0.1:8082/getProductInfo?productId=" + productId;
        String response = HttpClientUtils.sendGetRequest(url);
        System.out.println(response);

        return "success";
    }
}
```
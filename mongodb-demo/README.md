---
title: MongoDB的使用
date: 2017-9-11
categories: 
- 大数据
- Mongodb
tags:
- 大数据
- Mongodb
---

## 准备机器

```
操作系统：centos 7
机器：115.28.240.96
端口：27017
```

## 安装

### 下载MongoDB（64位）

```bash
wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
```

### 安装MongoDB（安装到/usr/local/目录下）

```bash
tar –zxvf mongodb-linux-x86_64-2.4.9.tgz -C /usr/local
mv mongodb-linux-x86_64-2.4.9 mongodb
cd mongodb
mkdir db # 创建数据库文件目录
mkdir logs # 创建MongoDB日志目录
cd bin
```

### 编辑mongodb.conf

```bash
vi mongodb.conf
```

```bash
# mongod进程存储数据目录，此配置仅对mongod进程有效。默认值为：/data/db
dbpath=/usr/local/mongodb/db
# logpath:日志目录
logpath=/usr/local/mongodb/logs/mongodb.log
# mongod侦听端口，默认值为27017
port=27017
# 后台方式运行mongodb
fork=true
# 关闭http接口
nohttpinterface=true
```

### 重新绑定mongodb的配置文件地址和IP

```bash
/usr/local/mongodb/bin/mongod --bind_ip 115.28.240.96 -f /usr/local/mongodb/bin/mongodb.conf
```

### 加入开机启动mongodb

```bash
vi /etc/rc.d/rc.local
/usr/local/mongodb/bin/mongod --bind_ip 115.28.240.96 -f /usr/local/mongodb/bin/mongodb.conf
```

### 进入mongodb看看是否能连接

```bash
/usr/local/mongodb/bin/mongo 115.28.240.96
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjfa44k7ylj21da0nq4de.jpg)

#### 查看数据列表

```bash
show dbs
```

#### 查看当前db版本

```bash
db.version()
```

### 客户端连接测试

```bash
使用Robomongo进行连接测试
下载地址：https://robomongo.org/
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjfad85000j21ru12en8r.jpg)

```bash
Mongodb中都以集合为主
```

### spring data for mongodb 简单连接mongodb 

>创建Maven工程

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjg2rew4v2j20y40towju.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjg2revfk1j20y40to0vy.jpg)

>pom.xml

```bash
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.matrix.momgodb</groupId>
  <artifactId>momgodb-example</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>momgodb-example</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.data</groupId>
      <artifactId>spring-data-mongodb</artifactId>
      <version>1.8.4.RELEASE</version>
    </dependency>
  </dependencies>
</project>
```

>TestMongoDB.java

```bash
package com.matrix.momgodb.momgodb_example;

import java.net.UnknownHostException;
import java.util.Set;

import org.junit.Test;

import com.mongodb.DB;
import com.mongodb.Mongo;

public class TestMongoDB {

	@Test
	public void testMongodb() {
		try {
			Mongo mongo = new Mongo("115.28.240.96", 27017);
			DB db = mongo.getDB("test");

			Set<String> collections = db.getCollectionNames();

			for (String name : collections) {
				System.out.println("collection=" + name);
			}
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}
	}
}
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjg3ghh6eqj21n217ok7y.jpg)

### spring data for mongodb 实现repo接口+mongoTemplate+CRUD操作

>下载spring的spring-data的子项目两个jar，分别是

```bash
spring-data-commons-1.10.0.RELEASE.jar
spring-data-mongodb-1.8.4.RELEASE.jar
```

```bash
<dependency>
	<groupId>org.springframework.data</groupId>
	<artifactId>spring-data-commons</artifactId>
	<version>1.10.0.RELEASE</version>
</dependency>
<dependency>
	<groupId>org.springframework.data</groupId>
	<artifactId>spring-data-mongodb</artifactId>
	<version>1.8.4.RELEASE</version>
</dependency>
```

>下载mongoDb的java驱动jar包

```bash
<dependency>
	<groupId>org.mongodb</groupId>
	<artifactId>mongo-java-driver</artifactId>
	<version>3.3.0</version>
</dependency>
```

### spring data for mongodb 分页查询
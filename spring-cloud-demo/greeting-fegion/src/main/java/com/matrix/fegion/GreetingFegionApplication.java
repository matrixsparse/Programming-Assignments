package com.matrix.fegion;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.feign.EnableFeignClients;

@SpringBootApplication
@EnableAutoConfiguration
@EnableFeignClients
public class GreetingFegionApplication {

    public static void main(String[] args) {
        SpringApplication.run(GreetingFegionApplication.class, args);
    }
}

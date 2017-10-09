package com.matrix.fegion.service;

import org.springframework.cloud.netflix.feign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * 声明远程服务接口
 */
@FeignClient(value = "SERVICE-SAY-HELLO")
public interface SayHelloService {

    @RequestMapping(value = "/sayHello", method = RequestMethod.GET)
    String sayHello(@RequestParam(value = "name") String name);
}

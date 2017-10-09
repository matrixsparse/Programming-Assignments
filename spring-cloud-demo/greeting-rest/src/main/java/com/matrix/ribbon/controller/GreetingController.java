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

package com.fomono.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class Welcome {
    @RequestMapping(value = "/")
    public ModelAndView welcomePage() {
        ModelAndView mav = new ModelAndView();
        return mav;
    }
}
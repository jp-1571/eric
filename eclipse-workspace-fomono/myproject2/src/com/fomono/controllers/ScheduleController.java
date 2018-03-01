package com.fomono.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ScheduleController {
    @RequestMapping(value = "/schedule")
    public ModelAndView schedulePage() {
        ModelAndView scheduleMav = new ModelAndView();
        return scheduleMav;
    }
}
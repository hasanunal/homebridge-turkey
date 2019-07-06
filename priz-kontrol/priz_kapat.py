#!/usr/bin/env python
import RPi.GPIO as GPIO
gpio_pin_number=20
GPIO.setmode(GPIO.BCM) # BCM pin numarasi
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT) 
GPIO.output(gpio_pin_number, GPIO.LOW)
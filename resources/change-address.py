#!/usr/bin/env python

import argparse
import RPi.GPIO as GPIO
import VL53L1X
import time

addr_current = 0x29
addr_1 = 0x33
addr_2 = 0x34
addr_3 = 0x35
addr_4 = 0x36

pin1 = 29
pin2 = 31
pin3 = 33
pin4 = 35
pin5 = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
    
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.HIGH)
GPIO.output(pin5, GPIO.HIGH)


GPIO.output(pin1, GPIO.LOW)
time.sleep(500)
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof.open()
tof.change_address(addr_1)
tof.close()

GPIO.output(pin2, GPIO.LOW)
time.sleep(500)
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof.open()
tof.change_address(addr_2)
tof.close()

GPIO.output(pin3, GPIO.LOW)
time.sleep(500)
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof.open()
tof.change_address(addr_3)
tof.close()

GPIO.output(pin4, GPIO.LOW)
time.sleep(500)
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof.open()
tof.change_address(addr_4)
tof.close()


GPIO.output(pin5, GPIO.LOW)
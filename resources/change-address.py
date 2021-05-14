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
    
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)
GPIO.output(pin5, GPIO.LOW)


GPIO.output(pin1, GPIO.HIGH)
time.sleep(1)
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof1.open()
tof1.change_address(addr_1)
tof1.close()

GPIO.output(pin2, GPIO.HIGH)
time.sleep(1)
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof2.open()
tof2.change_address(addr_2)
tof2.close()

GPIO.output(pin3, GPIO.HIGH)
time.sleep(1)
tof3 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof3.open()
tof3.change_address(addr_3)
tof3.close()

GPIO.output(pin4, GPIO.HIGH)
time.sleep(1)
tof4 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=addr_current)
tof4.open()
tof4.change_address(addr_4)
tof4.close()


GPIO.output(pin5, GPIO.HIGH)
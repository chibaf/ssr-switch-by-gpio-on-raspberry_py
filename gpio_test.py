import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# 11,12,13,15,16,18
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
#
GPIO.output(11, 1)
time.sleep(1)
GPIO.output(12, 1)
time.sleep(1)
GPIO.output(13, 1)
time.sleep(1)
GPIO.output(15, 1)
time.sleep(1)
GPIO.output(16, 1)
time.sleep(1)
GPIO.output(18, 1)
time.sleep(1)
#
GPIO.output(11, 0)
time.sleep(1)
GPIO.output(12, 0)
time.sleep(1)
GPIO.output(13, 0)
time.sleep(1)
GPIO.output(15, 0)
time.sleep(1)
GPIO.output(16, 0)
time.sleep(1)
GPIO.output(18, 0)
#
GPIO.cleanup()
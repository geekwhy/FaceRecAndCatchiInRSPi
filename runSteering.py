import RPi.GPIO as GPIO
from time import sleep
import sys
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
XPin = 11
YPin = 13
GPIO.setup(XPin, GPIO.OUT)
GPIO.setup(YPin, GPIO.OUT)

def RunStreering(pinName, angleNum):
    while angleNum >= 30 and angleNum <= 150:
        pwm = GPIO.PWM(pinName, 50)
        pwm.start(8)
        dutyCycle = angleNum * 0.062 + 1.5
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.5)
        pwm.stop()
        return

if __name__ == '__main__':
    for i in range(30, 150, 15):
        RunStreering(XPin, i)
        RunStreering(YPin, i)
    for i in range(150, 30, -15):
        RunStreering(XPin, i)
        RunStreering(YPin, i)
    RunStreering(XPin, 90)
    RunStreering(YPin, 90)
    GPIO.cleanup()
    
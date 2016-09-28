import RPi.GPIO as GPIO ## Import GPIO library
from random import randint

def led(status):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, status)
    # GPIO.cleanup()

def led_random():
    tab = [False,True]
    idx = randint(0,1)
    status = tab[idx]
    led(status)
    return status

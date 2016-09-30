import RPi.GPIO as GPIO ## Import GPIO library
import time
from random import randint
from threading import Thread

def led(status):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, status)

def led_random():
    tab = [False,True]
    idx = randint(0,1)
    status = tab[idx]
    led(status)
    return status

class Led_thread (Thread):
    """Thread in charge to blink the pi LED."""
    def __init__(self, thread_name):
        Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        status = False
        for idx in range (0,10):
            led(status)
            status = not status
            print "%s , %s" % ( self.thread_name, status )
            time.sleep(0.5)
"""
try:
    my_thread = Led_thread("blink_thread")
    # Starts the thread's activity
    my_thread.start()
    # Waits until the thread terminates
    my_thread.join()
except:
    print "Error : unable to start thread"
"""

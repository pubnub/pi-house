# Using PWM with RPi.GPIO

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode(GPIO.BCM)

PIN_LIVING = 4
PIN_PORCH = 17
PIN_FIREPLACE = 27

GPIO.setup(PIN_LIVING,GPIO.OUT)
GPIO.setup(PIN_PORCH,GPIO.OUT)
GPIO.setup(PIN_FIREPLACE,GPIO.OUT)

FREQ = 100 # frequency in Hz
FIRE_FREQ = 30 #  flickering effect

# Duty Cycle (0 <= dc <=100)

living = GPIO.PWM(PIN_LIVING, FREQ)
living.start(0)

porch = GPIO.PWM(PIN_PORCH, FREQ)
porch.start(0)

fire = GPIO.PWM(PIN_FIREPLACE, FIRE_FREQ)
fire.start(0)

# PubNub

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')

channel = 'pi-house'

def _callback(m, channel):
    print(m)

    dc = m['brightness'] * 10

    if m['item'] == 'light-living':
        living.ChangeDutyCycle(dc)

    elif m['item'] == 'light-porch':
        porch.ChangeDutyCycle(dc)

    elif m['item'] == 'fireplace':
        fire.ChangeDutyCycle(dc)

def _error(m):
  print(m)

pubnub.subscribe(channels=channel, callback=_callback, error=_error)

try:
    while 1:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)
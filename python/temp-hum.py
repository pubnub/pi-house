# -*- coding: utf-8 -*-
import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')
channel = 'sensor'

def callback(message):
    print(message)

#published in this fashion to comply with Eon
while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    message = {'temperature': t, 'humidity': h}
    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)
    pubnub.publish(channel=channel, message=message, callback=callback, error=callback)



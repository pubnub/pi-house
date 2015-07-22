# -*- coding: utf-8 -*-
import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')
channel = 'pi-house'

def callback(message):
    print(message)

#published in this fashion to comply with Eon
while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    temp='{0:0.1f}'.format(t)
    hum='{0:0.1f}'.format(h)
    print temp
    print hum
    message = {'temperature': temp, 'humidity': hum}
    pubnub.publish(channel=channel, message=message, callback=callback, error=callback)



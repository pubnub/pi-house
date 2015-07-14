#some background on the Pi house
##Introduction

We promised you that we will dig deeper into the individual hardware and software components of the Pi house. The pi house is a lego house that has a raspberry pi model B+ for a brain. It has lights, sensors and a door that can be controlled using a mobile device from anywhere in the world.

This post will focus on the temperature humidity sensor in the house. I will take you through the steps of setting up the hardware, hooking it up with PubNub, and finally viewing the readings on a browser. This is the first step in building a fully working IoT implementation, both on the hardware and software side.

DESCRIBE HOW IT WORKS WITH JOES IMAGE.


# How to use the sensor, how to hook it up?
## what sensor is this?

The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin.


## how to connect it to the Pi?

#### What you will need

1.The DHT22 sensor

![image](images/dht22.png)
2.3 jumper wires 
3.Breadboard  
4.4.7kΩ (or 10kΩ) resistor
5.Raspberry Pi B+ loaded with the Raspbian OS. 

Set up the circuit according to the following figure: 

![image](images/circuitdht22.png)

which translates to 

![image](images/breadboard.png)

I have connected to GPIO4 (pin7), pin 1 for the voltage (3v3) and pin 6 for ground. The resistor goes between the first two pins of the sensor. The third pin of the sensor need not be connected to anything.

## how do you read values from it?

We need to use Adafruits DHT library to be able to read the temperature values from the sensor.

The Python code to work with Adafruit's DHT sensors is available on [Github](https://github.com/adafruit/Adafruit_Python_DHT).


Open LXTerminal, and download and install the followings:

**Install Python:**
`pi@raspberrypi ~$ sudo apt-get install python-dev`

**Install pip:**
`pi@raspberrypi ~$ sudo apt-get install python-pip`


**Downloading the Adafruit DHT liibrary:**

`pi@raspberrypi ~$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
`pi@raspberrypi ~$ cd Adafruit_Python_DHT`

If you see an error that a package is already installed or at the latest version, don't worry you can ignore it and move on.

Next, to install the library execute:

`pi@raspberrypi ~$ sudo python setup.py install`

This should compile the code for the library and install it on your device so any Python program can access the Adafruit_DHT python module.

The code snippet below makes the pi read the humidity and temperature values from the sensor and print it out.

```
h,t = dht.read_retry(dht.DHT22, 4)
print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)

```

So, now we have a sensor that keeps measuring data but not doing much with it. You want to be able to view this information on a browser or mobile device in real time, to be able to do something meaningful with it. Enter PubNub. 

# What is PubNub doing here? How to use it?
## what is PubNub?

## where would you use it?

PubNub is a secure data stream network, that provides easy to use API to build and scale real time applications. PubNub is used in several verticals such as home automation, taxi dispatch, financial services, gaming and many more. 

This Pi house is all about IoT, and the IoT is all about the devices communicating with each other in real time. PubNub is what enables that communication between devices. Whether its a mobile device or a web broswer talking to embedded devices, sensors or any other device, PubNub glues them  together.

## what are you using it here for?

In this specific example, you use the browser to communicate with the sensors and the Pi, to ask for temperature and humidity values. The sensor measures them, and sends it back over PubNub, allowing you to visualize it on your browser. 

## how do you use it?

#### Installing PubNub

**install PubNub:**
`pi@raspberrypi ~$ sudo pip install pubnub`

For an in depth introduction to the Pi and PubNub, check this [blog](http://www.pubnub.com/blog/internet-of-things-101-getting-started-w-raspberry-pi/).

Make sure you have [signed up for PubNub](https://www.pubnub.com/get-started/) to obtain your pub/sub keys.

You make sure you import the right libraries needed for this program.

```
	import os
	import time
	import sys
	from Pubnub import Pubnub
	import Adafruit_DHT as dht
	pubnub = Pubnub(publish_key='demo', subscribe_key='demo')
```





# how to use the UI?
## PubNub console?
## whats the deal with visualization?
## how to use this?

## conclusion

We will be posting more tutorials on how to control the lights in the house, how to change their intensity and also how to flicker them. Stay tuned for more pi goodyness.

 

 
# importing libraries
import paho.mqtt.client as mqttClient
import os
import socket
import ssl
from time import sleep
from random import uniform
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print "Connected to CloudMqtt"
    connflag = True
    print("Connection returned result: " + str(rc))

def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))

    # initialize GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

broker_address= "m23.cloudmqtt.com"
port = 13615
user = "qrozvxtl"
password = "F3XABhi9x7fJ"

mqttc =mqttClient.Client("Python")
mqttc.username_pw_set(user, password=password)    #set username and password

#t1=datetime.datetime.now()
#print("time of connecting "+str(t1))
mqttc.on_connect= on_connect                      # callback function
#t2=datetime.datetime.now()
#print("time of receving "+str(t2))
mqttc.on_message=on_message

t1=datetime.datetime.now()
print("time ofconnecting "+str(t1))
mqttc.connect(broker_address, port=port)          #connect to broker
t2=datetime.datetime.now()
print("time of reciving "+str(t2))



mqttc.loop_start()                                          # Start the loop
instance = dht11.DHT11(pin=17)
while 1==1:
    sleep(5)
    if connflag == True:
        result = instance.read()
        if result.is_valid():
            #print("Last valid input: " + str(datetime.datetime.now()))
            #print("Temperature: %d C" % result.temperature)
            #print("Humidity: %d %%" % result.humidity)
                               # Generating Temperature Readings
           # x=str(datetime.datetime.now())
	    z=str(result.humidity)
	    y="temp(C): "+str(result.temperature) + "  humidity :"+z
            t5=datetime.datetime.now()
            mqttc.publish("temperature:", y , qos=1)
            t6=datetime.datetime.now()
	    print("date and time before sending data " + str(t5))
            print("date and time after receiving ack " +str(t6))
	    print("msg sent:DHT11 reading  " + "%s" % y)

    else:
                        print("waiting for connection...")

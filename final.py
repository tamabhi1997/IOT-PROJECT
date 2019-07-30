
# importing libraries
import paho.mqtt.client as mqttClient
import os
import socket
import ssl


def on_connect(client, userdata, flags, rc):                # func for making connection
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )                              # Subscribe to all topics

def on_message(client, userdata, msg):                      # Func for receiving msgs
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))


broker_address= "m23.cloudmqtt.com"
port = 13615
user = "qrozvxtl"
password = "F3XABhi9x7fJ"

mqttc =mqttClient.Client("p1")
mqttc.username_pw_set(user, password=password)    #set username and password

mqttc.on_connect= on_connect                      #attach function to callback
mqttc.on_message=on_message
mqttc.connect(broker_address, port=port)          #connect to broker

mqttc.loop_forever()

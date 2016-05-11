#This is code for Laptop 3 Client to display messages for all the topics in Assignment 3

import paho.mqtt.client as mqtt
import time
from datetime import datetime
logFile = open('Logs.txt', 'a')
logData=''
statusStr=''
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("lightsensor",2)
    client.subscribe("threshold",2)
    client.subscribe("Status/Arduino",2)
    client.subscribe("Status/RPi",2)
    client.subscribe("lightStatus",2)


#call back function for when a publish message for LED status is received from the server.
def on_message_LedStatus(client, userdata, msg):
    timeStamp=str(datetime.now())
    logData=timeStamp+"---"+msg.topic+" "+str(msg.payload)
    logFile.write(str(logData))
    logFile.write("\n")
    if(msg.payload=='TurnOn'):
        statusStr="** Smart LED was Turned ON at"+timeStamp+' **'
    else:
        statusStr="** Smart LED was Turned OFF at "+timeStamp+' **'
    print(statusStr)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    logData=str(datetime.now())+"---"+msg.topic+" "+str(msg.payload)
    print(logData)
    logFile.write(str(logData))
    
    logFile.write("\n")

    #print(msg)

client = mqtt.Client(client_id='Laptop 3')
#for keeping a track of when LED was turned on and turned off
client.message_callback_add("lightStatus", on_message_LedStatus)
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.10.9", 1883, 60)

print("Connected")

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
client.loop_forever()
logFile.close()

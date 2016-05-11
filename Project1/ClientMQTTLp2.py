#This is code for Laptop 2 Client to publish messages to topic lightsensor,threshold,Status/Arduino


import paho.mqtt.client as mqtt
import serial
import math
import time
# The callback for when the client receives a CONNACK response from the server.
preLDRvalue = 0.0
prePOTvalue = 0.0
diffLdr=0.0
diffPot=0.0
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish("Status/Arduino", payload="online", qos=0, retain=True)
    #client.will_set("Status/Arduino", payload="offline", qos=0, retain=True)

    client.subscribe("lightsensor")
    client.subscribe("threshold")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print("Normal Message"+msg.topic+" "+str(msg.payload))

def on_message_light(mosq, obj, msg):
    #print("LIGHT MESSAGES: "+msg.topic+" "+" "+str(msg.payload))
    global preLDRvalue
    preLDRvalue = float(msg.payload)

def on_message_threshold(mosq, obj, msg):
    #print("THRESHOLD MESSAGES: "+msg.topic+" "+" "+str(msg.payload))
    global prePOTvalue
    prePOTvalue = float(msg.payload)

client = mqtt.Client(client_id='Laptop 2_Arduino')			#client banaya
client.on_connect = on_connect #call back
client.message_callback_add("lightsensor", on_message_light)
client.message_callback_add("threshold", on_message_threshold)
client.on_message = on_message
# setting Last will for laptop 2 client for topic Status/Arduino.
client.will_set("Status/Arduino", payload="offline", qos=2, retain=True)
client.connect("172.20.10.7", 1883, 60)

client.loop_start()
ser = serial.Serial('COM3', 9600)



while True:
    LDR0 = ser.readline()
    #print(str(LDR0))
    if LDR0[:8] == "LDRValue":
        ldrv = LDR0[8::]
        #print int(ldrv)
        ldrvNorm=int(ldrv)/160.00
        #print ldrvNorm
        diffLdr=abs(preLDRvalue-ldrvNorm)
        #print"LightDiff---",diffLdr
        if diffLdr > 0.5:
            client.publish("lightsensor", payload=ldrvNorm, qos=2, retain=True)
            print "ldrv: ",ldrvNorm
            print"LightSensor Value published"


    if LDR0[:8] == "PotValue":
        potv = LDR0[8::]

        potvNorm=int(potv)/1024.00
        diffPot=abs(prePOTvalue-potvNorm)
        #print "PotDiff---",diffPot
        if diffPot > 0.15:
            client.publish("threshold", payload=potvNorm, qos=2, retain=True)
            print "potv: ",potvNorm
            print"Threshold Value published"
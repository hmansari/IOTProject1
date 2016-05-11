import paho.mqtt.client as mqtt
import time

LightStatus = False
preLightStatus = False
LDRValue = 0.0
ThresholdValue = 0.0
# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish("Status/RPi", payload="online", qos=2, retain=True)
    #client.will_set("Status/Arduino", payload="offline", qos=0, retain=True)

    client.subscribe("lightsensor", 2)
    client.subscribe("threshold", 2)
    client.subscribe("lightStatus", 2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

  print("Normal Message: "+msg.topic+" "+str(msg.payload))

def on_message_light(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # lightsensor
    global LDRValue
    global LightStatus
    LDRValue = float(msg.payload)
    if (LDRValue >= ThresholdValue):
      LightStatus = False
    else:
      LightStatus = True
    print("LIGHT MESSAGES: "+msg.topic+" "+" "+str(msg.payload))

def on_message_threshold(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # threshold
    
    global ThresholdValue
    ThresholdValue= float(msg.payload)
    if (LDRValue >= ThresholdValue):
      global LightStatus
      LightStatus = False
    else:
      global LightStatus
      LightStatus = True
    print("THRESHOLD MESSAGES: "+msg.topic+" "+" "+str(msg.payload))

def on_message_lightstatus(mosq, obj, msg):
	# This callback will only be called for messages with topics that match
    # threshold
    #print(msg.topic+": "+str(msg.payload))
    
    if msg.payload == 'TurnOn':
      global preLightStatus
      preLightStatus = True
    else:
      global preLightStatus
      preLightStatus = False

def on_message_StatusArduino (mosq, obj, msg):
	print(msg.topic+": "+str(msg.payload))

client = mqtt.Client(client_id = 'mqtt_raspberryPi')       #client object   
client.on_connect = on_connect #call back
client.message_callback_add("lightsensor", on_message_light)
client.message_callback_add("threshold", on_message_threshold)
client.message_callback_add("lightStatus", on_message_lightstatus)
client.message_callback_add("Status/Arduino", on_message_StatusArduino)
client.on_message = on_message


client.will_set("Status/RPi", payload="offline", qos=2, retain=True)
client.connect("172.20.10.2", 8080, 60)

#client.publish("lightStatus", payload = "TurnOff", qos = 2, retain = True)

client.loop_start()
#print LightStatus
#print preLightStatus
while True:
  if (LightStatus != preLightStatus):
    print "LightStatus", LightStatus
    print "preLightStatus", preLightStatus
    if (LightStatus):
   		client.publish("lightStatus", payload = "TurnOn", qos = 2, retain = True)
    else:
      client.publish("lightStatus", payload = "TurnOff", qos = 2, retain = True)
    global preLightStatus
    preLightStatus = LightStatus
client.disconnect()
client.loop_stop()

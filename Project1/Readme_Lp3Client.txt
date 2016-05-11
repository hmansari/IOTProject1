IDE used : PyCharm
Python version: Python 2.7

Requirement:
1. The laptop3 should be in the same subnet network as all the other devices used as a part of this assignment task.
2. MQTT Client library is installed to all MQTT clients in our setup. First, we cloned the git repository of MQTT Paho. The following are the commands used:
	> git clone git://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git
	> cd org.eclipse.paho.mqtt.python
	> python setup.py install

Execution order
1. Run the broker on Laptop1 and put it into a listening state.
2. Run the ClientMQTTLp3.py code for client on Laptop 3 to connect to broker and subscribe to topics.


For Run:
In CLI:
> python ClientMQTTLp3.py 


Using the python code, Laptop3 connects to the broker as a MQTT client and subscribes to the following topics:
lightsensor, threshold, Status/Arduino, Status/RPi,lightStatus. 
Client on Laptop3 also displays all the messages received from the broker for the subscribed topics. It also keeps a track of when the LED was turned on and turned Off.
The code also creates a log file named "LogSmartLED.txt"
The file received will be created in the same directory where the code is saved.


Submitted by:

Haris Ansari 
hmansari@ncsu.edu

Jina Jain
jhjain@ncsu.edu

Arpita Awasthi
aawasth2@ncsu.edu

Pranjali Chumbhale
pchumbh@ncsu.edu

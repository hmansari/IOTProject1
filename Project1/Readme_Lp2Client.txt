IDE used : PyCharm
Python version: Python 2.7

Requirement:
1. The laptop3 should be in the same subnet network as all the other devices used as a part of this assignment task.
Serial connection with arduino.
2. MQTT Client library is installed to all MQTT clients in our setup. First, we cloned the git repository of MQTT Paho. The following are the commands used:
	> git clone git://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git
	> cd org.eclipse.paho.mqtt.python
	> python setup.py install

Execution order
1. Run the broker on Laptop1 and put it into a listening state.
2. Connect Arduino to laptop 2 via serial connection.
3. Run the ClientMQTTLp2.py code for client on Laptop 2 to connect to broker and publish to topics.


For Run:
In CLI:
> python ClientMQTTLp2.py 


Using the python code, Laptop2 connects to the broker as a MQTT client and publishes to the following topics:
lightsensor, threshold, Status/Arduino. 
Client on Laptop2 publishes values to topics lightsensor and threshold only when the values change beyond a certain threhold.
Status/Arduino topic publishes data for online/offline status of arduino.


Submitted by:

Haris Ansari 
hmansari@ncsu.edu

Jina Jain
jhjain@ncsu.edu

Arpita Awasthi
aawasth2@ncsu.edu

Pranjali Chumbhale
pchumbh@ncsu.edu

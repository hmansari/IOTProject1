Editor Used : SublimeText
Board Used: Raspberry Pi
Libraries: paho.mqtt.client

Requirement:
1. MQTT Client library is installed to all MQTT clients in our setup. First, we cloned the git repository of MQTT Paho. The following are the commands used:
	> git clone git://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git
	> cd org.eclipse.paho.mqtt.python
	> python setup.py install
2. The raspberry pi should be in the same subnet as the other devices.

For Run:
3. Run the file rpi.py by typing the following commands in the terminal
	cd ./Documnets
	python rpi.py
	
The Raspberry pi publishes 2 topics - Status/RPi (online and offline) and lightStatus (TurnOn and TurnOff). It is subscribed to lightsensor and threshold topic. It publishes to the lightStatus topic if it detects a significant change in the ambient light.

Submitted by:

Haris Ansari 
hmansari@ncsu.edu

Jina Jain
jhjain@ncsu.edu

Arpita Awasthi
aawasth2@ncsu.edu

Pranjali Chumbhale
pchumbh@ncsu.edu

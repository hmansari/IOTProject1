IDE Used : Intel XDK IoT Edition
Board Used: Intel Edison
Platform Used: Node.js
Libraries needed: mraa, mqtt

Selecting the board and port:
1. Connect the Edison to laptop using the OTG and console.
2. Start XDK. Connect to the Edison device from the XDK using the option 

Compiling and uploading the code:
3. Compile and upload the code by clicking on the upward arrow icon on XDK.

Running the code:
4. Click on the start icon.

Edison is subscribed to the topics Status/Arduino, Status/RPi and lightStatus. Based on the messages published, Edison will control 3 LEDs. The LED corresponding to Arduino status, blue led, glows if Arduino is online. The LED corresponding to Raspberry Pi status, red led, glows if Raspberry Pi is online. The Smart Light, green led, glows if Raspberry Pi is online and the Light Staus is TurnOn.


Submitted by:

Haris Ansari 
hmansari@ncsu.edu

Jina Jain
jhjain@ncsu.edu

Arpita Awasthi
aawasth2@ncsu.edu

Pranjali Chumbhale
pchumbh@ncsu.edu

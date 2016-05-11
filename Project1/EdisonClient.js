/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)


var mraa= require('mraa'); //Include MRAAlibrary
var mqtt=require('mqtt');

// Find MRAA pin mappings at https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-e-mraa-pin-table

var led1= new mraa.Gpio(33);  //LED - Green Led - GP48
var led2 = new mraa.Gpio(48); // Arduino - BLUE led - GP15
var led3 = new mraa.Gpio(32); // RED led - RPI - GP46

led1.dir(mraa.DIR_OUT);
led2.dir(mraa.DIR_OUT);
led3.dir(mraa.DIR_OUT);

//Clear all LEDs
led1.write(0);
led2.write(0);
led3.write(0);

var client = mqtt.connect({host:'172.20.10.7', port:'1883',  protocolId: 'MQIsdp', protocolVersion: 3, keepalive: 60, clientId:'mqtt_edison'});

client.on('connect', function () {
    console.log('connected')
  client.subscribe({'lightStatus': 2,'Status/Arduino': 2,'Status/RPi':2});
});

client.on('message', function(topic, message) {
  // message is Buffer 
  console.log(topic.toString() + ': ' + message.toString());
  switch (topic)
      {
      case 'Status/Arduino':
              if (message == 'online')
                led2.write(1);
              else led2.write(0);
              break;
      
      case 'Status/RPi':
              if (message == 'online')
                led3.write(1);
              else {
                  led1.write(0);
                  led3.write(0);
             
      } break;
      case 'lightStatus':
              if (message == 'TurnOn')
                led1.write(1);
              else led1.write(0);
               break;
      }
  
});

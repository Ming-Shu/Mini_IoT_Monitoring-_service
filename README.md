# Mini_IoT_Monitoring_service

How to build a simply monitoring system for your IoT device.
This code  about creating a monitoring and analytics system for IoT system.We used opcua and mqtt design  this it .This system will auto send machine information to any monitor device.

Package & Tool:
                                  1. Installing Mosquitto
                                  2. paho-mqtt
                                  3. FreeOpcUa

Operating System    :  Ubuntu 18.04

Python version      :  3.6.9


Note:

Commmand line:

     For Python version 3.x+
     
              sudo apt-get install python3-dev

    For Mosquitto  
    
              sudo apt update
              sudo apt install mosquitto mosquitto-clients
              #By default, Ubuntu will start the Mosquitto service after install. Let’s test the default configuration. We’ll use one of the Mosquitto clients we just installed to subscribe to a topic on our broker.
 
    For paho-mqtt 
    
             pip3 install paho-mqtt
             
    For FreeOpcUa    
    
            pip install opcua
            apt install python-opcua        # Library
            apt install python-opcua-tools  # Command-line tools

Sysyem Architecture:
![image](https://github.com/Ming-Shu/Mini_IoT_Monitoring_service/blob/main/Architecture.PNG)


Reference:  

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-18-04

https://pypi.org/project/paho-mqtt/

https://ithelp.ithome.com.tw/articles/10227131

https://github.com/FreeOpcUa/python-opcua

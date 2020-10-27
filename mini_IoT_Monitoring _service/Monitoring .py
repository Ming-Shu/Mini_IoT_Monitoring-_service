import paho.mqtt.client as mqtt 
import json  
import sys,time
import pprint

from opcua import Client
from opcua import ua

if __name__ == "__main__":

	client = Client("opc.tcp://localhost:4840/freeopcua/server/")

	_g_cst_ToMQTTTopicServerIP = "localhost"
	_g_cst_ToMQTTTopicServerPort = 1883 #port
	_g_cst_MQTTTopicName = "MYTOPIC" #TOPIC name
	data = "Temperature" 
	mqttc = mqtt.Client("python_pub")
	mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort) 
	try:
		res = client.connect()
		# Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
		root = client.get_root_node()
		print("Objects node is: ", root)

		# Node objects have methods to read and write node attributes as well as browse or populate address space
		print("Children of root are: ", root.get_children())

		# Now getting a variable node using its browse path
		while(1):			
			val = root.get_children()[0].get_children()[1].get_variables()[0].get_value()
			print("val",val)
			payload = {"data":data,"value":val}
			print("payload: ",json.dumps(payload))
			mqttc.publish(_g_cst_MQTTTopicName, json.dumps(payload), qos=0)
			time.sleep(5)
			

	finally:
		client.disconnect()

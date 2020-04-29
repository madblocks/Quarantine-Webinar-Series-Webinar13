# Publish Data

import paho.mqtt.client as mqtt

# Create a Client Object
client=mqtt.Client()

# Client has to be connected with Broker
try:
	client.connect('broker.hivemq.com',1883) 
	print ('Broker Connected')
except:
	print ('Broker Connection Failure')

while True:
	t=str(raw_input('Enter message: '))
	client.publish('iot/webinar',str(t))




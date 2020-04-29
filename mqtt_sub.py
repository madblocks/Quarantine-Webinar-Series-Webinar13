import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

# Create a Client Object
client=mqtt.Client()

# Connect with Broker
try:
	client.connect('broker.hivemq.com',1883)
	print ('Broker Connected')
except:
	print ('Broker Connection Failure')

client.subscribe('iot/webinar')

def notification(client,userdata,msg):
 print(msg.payload) # prints the msg from pub
 if (msg.payload=='ledon'):
	print ('LED is requested to be ON')
	GPIO.output(2,1)
 elif (msg.payload=='ledoff'):
	print ('LED is requested to be OFF')
	GPIO.output(2,0)

client.on_message=notification
client.loop_forever() # pushing subscriber to be ready until subscriber app gets closed

import board
import digitalio
from adafruit_apds9960.apds9960 import APDS9960
import time
import paho.mqtt.client as mqtt
import uuid


client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

topic = 'IDD/proximity'

available = False

while True:
	print(f'{apds.proximity}')

	if apds.proximity > 5 and not available:
		client.publish(topic, "I'm available now, feel free to reach out.")
		available = True
	elif 0 <= apds.proximity <= 5 and available:
		client.publish(topic, "I'm away.")
		available = False

	time.sleep(.5)

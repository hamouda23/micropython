from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep

CLIENT_NAME = 'blue'
BROKER_ADDR = '192.168.1.180'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive = 60)
mqttc.connect()

btn = Pin(0)
BTN_TOPIC = CLIENT_NAME.encode() + b'/btn/0'

while True :
    mqttc.publish(BTN_TOPIC, str(btn.value()).encode())
    sleep(0.5)
                  
                  
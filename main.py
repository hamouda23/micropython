from umqtt.simple import MQTTClient
from machine import Pin
import dht
from time import sleep

CLIENT_NAME = 'DHT11'
BROKER_ADDR = '192.168.1.180'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive = 60)
mqttc.connect()

btn = Pin(0)
BTN_TOPIC = CLIENT_NAME+"/Temp/Humid"

dht = dht.DHT11(Pin(14))

while True :
    try:
        dht.measure()
        t = dht.temperature()
        h = dht.humidity()
        if isinstance(t,float) and isinstance(h, float) :
            msg = (b'{},{}'.format(t,h))
            mqttc.publish(BTN_TOPIC, msg)
        else :
            print ('Capteur non valide')
    except OSError:
        print('Erreur de lecture de capteur.')
    sleep(5)
                  
                  
from machine import Pin, Timer
import dht

dht = dht.DHT11(Pin(14))

def take_mesear_isr(event):
    dht.measure()
    print("Temp :",dht.temperature(),"°C","  Humid :",dht.humidity(),"%")
    
dht_timer=Timer(1)

dht_timer.init(period=5000, mode=Timer.PERIODIC, callback=take_mesear_isr)
    
from machine import Pin, Timer
import dht
import mon_wif
import network


sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(mon_wif.ssid, mon_wif.password)
dht = dht.DHT11(Pin(14))

def take_mesear_isr(event):
    if sta.isconnected()==True:
        dht.measure()
        print("Temp :",dht.temperature(),"°C","  Humid :",dht.humidity(),"%")
    
    
dht_timer=Timer(1)

dht_timer.init(period=5000, mode=Timer.PERIODIC, callback=take_mesear_isr)
    
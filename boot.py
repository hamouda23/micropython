#dht = dht.DHT11(Pin(14))

def connect():
    sta = network.WLAN(network.STA_IF)

    if not sta.isconnected():
        sta.active(True)
        sta.connect(mon_wif.ssid, mon_wif.password)
        while not sta.isconnected():
            pass # wait till connection
    print('La configuration de réseau : ', sta.ifconfig())
        #dht.measure()
        #print("Temp :",dht.temperature(),"°C","  Humid :",dht.humidity(),"%")
        
connect()  
    
#dht_timer=Timer(1)

#dht_timer.init(period=5000, mode=Timer.PERIODIC, callback=take_mesear_isr)
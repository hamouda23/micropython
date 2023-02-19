from machine import Pin

led = Pin(13, Pin.OUT)
sw  = Pin(0, Pin.IN)

while True :
    if (sw.value() == 1):
        led.off()
        
    else :
        led.on()
        
        
from machine import Pin
from time import sleep

led = Pin(13, Pin.OUT)
sw  = Pin(0,Pin.IN)

def handel_interru(pin):
    led.value(not led.value())
    
    
sw.irq(trigger=Pin.IRQ_FALLING, handler = handel_interru)

from machine import Pin
from time import sleep_ms
sensor_ir=Pin(2,Pin.IN)
while True :
    print(sensor_ir.value())
    sleep_ms(500)
from hcsr04 import SR04
from machine import Pin
import time

# Define the ultrasonic sensors
SR_LEFT = SR04()
SR_RIGHT = SR04()
SR_FORWARD = SR04()


def getSonar():
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    
    while not echoPin.value():
        pass
    
    pingStart = time.ticks_us()
    
    while echoPin.value():
        pass
    
    pingStop = time.ticks_us()
    pingTime = time.ticks_diff(pingStop, pingStart)
    distance = pingTime*soundVelocity//2//10000
    return int(distance)

time.sleep_ms(2000)

while True:
    time.sleep_ms(500)
    print('Distance: ', getSonar(), ' cm')
from dcmtor import DCMotor       
from machine import Pin, PWM   
from time import sleep_ms   
frequency = 15000       
pin1 = Pin(2, Pin.OUT)    
pin2 = Pin(15, Pin.OUT)     
enable = PWM(Pin(13), frequency)      
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)
dc_motor.forward(50)    
sleep_ms(10000)        
dc_motor.stop()  
sleep_ms(10000)    
dc_motor.backwards(100)  
sleep_ms(10000)       
dc_motor.forward(60)
sleep_ms(10000)
dc_motor.stop()
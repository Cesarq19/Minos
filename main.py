from machine import Pin, PWM
from time import sleep_ms
from stepper import DCMotor

frequency = 15000 
IN1 = Pin(0, Pin.OUT)
IN2 = Pin(1, Pin.OUT)
enable1 = PWM(Pin(4), frequency)

IN3 = Pin(2, Pin.OUT)
IN4 = Pin(3, Pin.OUT)
enable2 = PWM(Pin(5),frequency)

motorA = DCMotor(IN1, IN2, enable1) # Configurar motor A con los pines 14 y 27
motorB = DCMotor(IN3, IN4, enable2) # Configurar motor B con los pines 26 y 25

while True:
    motorB.forward(100)
    motorA.forward(100)
    sleep_ms(2000)
    motorB.backwards(100)
    motorA.backwards(100)
    sleep_ms(2000)
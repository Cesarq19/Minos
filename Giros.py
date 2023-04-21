#Imports
from machine import Pin, PWM
from time import sleep_ms
from stepper import DCMotor

#Variables Constantes
frequency = 15000

# Pines a usar
IN1 = Pin(34, Pin.OUT)
IN2 = Pin(35, Pin.OUT)

IN3 = Pin(33, Pin.OUT)
IN4 = Pin(25, Pin.OUT)

#Pines Sensores
IR1 = Pin(36, Pin.IN)
IR2 = Pin(4, Pin.IN)
IR3 = Pin(5, Pin.IN)

Trig1 = Pin(22, Pin.OUT)
Trig2 = Pin(3, Pin.OUT)
Trig3 = Pin(19, Pin.OUT)

Echo1 = Pin(1, Pin.IN)
Echo2 = Pin(21, Pin.IN)
Echo3 = Pin(18, Pin.IN)

#PWM
EN1 = PWM(Pin(39), frequency)
EN2 = PWM(Pin(32), frequency)

#Motores
motorA = DCMotor(IN1, IN2, EN1) 
motorB = DCMotor(IN3, IN4, EN2)

#Posibles Giro IR
while True:
    obstaculo_derecha = IR1.value()
    obstaculo_izquierda = IR3.value()
    if not obstaculo_derecha:
        motorA.forward(100)
        motorB.stop()
    elif not obstaculo_izquierda:
        motorA.stop()
        motorB.forward(100)
    elif( obstaculo_izquierda and obstaculo_derecha):
        motorA.stop()
        motorB.stop()
    else:
        motorA.forward(100)
        motorB.forward(100)
        
    
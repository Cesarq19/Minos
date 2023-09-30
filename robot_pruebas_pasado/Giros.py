#Imports
from machine import Pin, PWM
from time import sleep_ms
from stepper import DCMotor
from hcsr04 import SR04
# Variables Constantes
frequency = 15000

# Pines a usar
IN1 = Pin(34, Pin.OUT)
IN2 = Pin(35, Pin.OUT)

IN3 = Pin(33, Pin.OUT)
IN4 = Pin(25, Pin.OUT)

# Pines Sensores
#Infrarrojo
IR1 = Pin(36, Pin.IN)
IR2 = Pin(4, Pin.IN)
IR3 = Pin(5, Pin.IN)

#Ulstrasonico
Trig1 = Pin(22, Pin.OUT)
Trig2 = Pin(3, Pin.OUT)
Trig3 = Pin(19, Pin.OUT)

Echo1 = Pin(1, Pin.IN)
Echo2 = Pin(21, Pin.IN)
Echo3 = Pin(18, Pin.IN)

# Ultrasonico variables
US1 = SR04(Trig1,Echo1)
US2 = SR04(Trig2,Echo2)
US3 = SR04(Trig3,Echo3)

# PWM
EN1 = PWM(Pin(39), frequency)
EN2 = PWM(Pin(32), frequency)

# Motores
motorA = DCMotor(IN1, IN2, EN1) 
motorB = DCMotor(IN3, IN4, EN2)

# Posibles Giro IR
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
    # Esperar un poco antes de volver a leer los sensores
    sleep_ms(50)
        
# Giros usando sensor Ultrasonico
        
# Definir la distancia deseada a la pared
distancia_objetivo = 10

while True:
    
    # Leer distancias a las paredes
    distancia_derecha = US1.distanceCM()
    distancia_frente = US2.distanceCM()
    distancia_izquierda = US3.distanceCM()

    # Comprobar si hay paredes a la derecha y frente
    if distancia_derecha < distancia_objetivo and distancia_frente < distancia_objetivo and distancia_izquierda > distancia_objetivo:
        # Giro a la izquierda
        motorA.backward(100)
        motorB.forward(100)
        
    # Comprobar si hay paredes a la izquierda y frente
    elif distancia_izquierda < distancia_objetivo and distancia_frente < distancia_objetivo and distancia_derecha > distancia_objetivo:
        # Giro a la Derecha
        motorB.backward(100)
        motorA.forward(100)
        
    # Comprobar si hay pared a la derecha
    elif distancia_derecha < distancia_objetivo and distancia_izquierda > distancia_objetivo:
        # Giro a la izquierda
        motorA.backward(100)
        motorB.forward(100)
        
    # Comprobar si hay pared a la izquierda
    elif distancia_izquierda < distancia_objetivo and distancia_derecha > distancia_objetivo:
        # Giro a la derecha
        motorB.backward(100)
        motorA.forward(100)
        
    # Comprobar si hay pared a la izquierda derecha y frente
    elif distancia_derecha < distancia_objetivo and distancia_frente < distancia_objetivo and distancia_izquierda < distancia_objetivo:
        # Giro a la derecha
        motorB.backward(100)
        motorA.forward(100)
        
    # Si no hay paredes al frente
    elif distancia_derecha < distancia_objetivo and distancia_frente > distancia_objetivo and distancia_izquierda < distancia_objetivo:
        # Giro a la derecha
        motorB.forward(100)
        motorA.forward(100)

    # Sin paredes
    else:
        motorA.stop(100)
        motorB.stop(100)
    
    # Esperar un poco antes de volver a leer los sensores
    sleep_ms(50)
    
from machine import Pin
import time
from math import sin, cos

# Configuración de los pines para los encoders
pin_encoder_izquierdo = Pin(36, Pin.IN)
pin_encoder_derecho = Pin(39, Pin.IN)

# Configuración de los pines para el control de los motores
pin_motor_izquierdo_1 = Pin(23, Pin.OUT)
pin_motor_izquierdo_2 = Pin(22, Pin.OUT)
pin_motor_derecho_1 = Pin(19, Pin.OUT)
pin_motor_derecho_2 = Pin(18, Pin.OUT)


# Variables para almacenar el estado anterior de los encoders
estado_anterior_izquierdo = 0
estado_anterior_derecho = 0

# Constantes relacionadas con el encoder
ranuras_por_vuelta = 24
radio_llanta = 3.9  # Radio de la llanta en cm

# Constantes de control PID
kp = 1.0  # Ganancia proporcional
ki = 0.0  # Ganancia integral
kd = 0.0  # Ganancia derivativa

# Variables de control PID
error_anterior = 0
integral = 0

# Variables para el control de movimiento
distancia_recorrida_izquierda = 0
distancia_recorrida_derecha = 0
posicion_x = 0  # Posición actual en el eje x del robot
posicion_y = 0  # Posición actual en el eje y del robot
angulo_actual = 0  # Ángulo actual de orientación del robot

# Función de interrupción para el encoder izquierdo
def handle_interrupt_izquierdo(pin):
    global estado_anterior_izquierdo, distancia_recorrida_izquierda, giro_izquierdo
    estado_actual_izquierdo = pin.value()
    if estado_actual_izquierdo != estado_anterior_izquierdo:
        distancia_recorrida_izquierda += 2 * 3.1416 * radio_llanta / ranuras_por_vuelta
    estado_anterior_izquierdo = estado_actual_izquierdo

# Función de interrupción para el encoder derecho
def handle_interrupt_derecho(pin):
    global estado_anterior_derecho, distancia_recorrida_derecha, giro_derecho
    estado_actual_derecho = pin.value()
    if estado_actual_derecho != estado_anterior_derecho:
        distancia_recorrida_derecha += 2 * 3.1416 * radio_llanta / ranuras_por_vuelta
    estado_anterior_derecho = estado_actual_derecho

# Configurar las interrupciones para los encoders
pin_encoder_izquierdo.irq(handler=handle_interrupt_izquierdo, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
pin_encoder_derecho.irq(handler=handle_interrupt_derecho, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# Funciones para controlar los movimientos del robot
def mover_adelante(distancia):
    global distancia_recorrida_izquierda, distancia_recorrida_derecha, posicion_x, posicion_y
    distancia_objetivo = distancia
    distancia_recorrida_inicial_izquierda = distancia_recorrida_izquierda
    distancia_recorrida_inicial_derecha = distancia_recorrida_derecha
    while (distancia_recorrida_izquierda - distancia_recorrida_inicial_izquierda) < distancia_objetivo:
        error = (distancia_recorrida_izquierda - distancia_recorrida_inicial_izquierda) - (distancia_recorrida_derecha - distancia_recorrida_inicial_derecha)
        velocidad = kp * error
        controlar_velocidad(velocidad)
        actualizar_posicion()
        time.sleep(0.01)
    detener_motores()

def girar(angulo):
    global angulo_actual
    angulo_objetivo = angulo
    angulo_inicial = angulo_actual
    while abs(angulo_actual - angulo_inicial) < angulo_objetivo:
        error = angulo_objetivo - (angulo_actual - angulo_inicial)
        velocidad = kp * error
        controlar_giro(velocidad)
        actualizar_posicion()
        time.sleep(0.01)
    detener_motores()

def controlar_velocidad(velocidad):
    if velocidad > 0:
        pin_motor_izquierdo_1.on()
        pin_motor_izquierdo_2.off()
        pin_motor_derecho_1.on()
        pin_motor_derecho_2.off()
    elif velocidad < 0:
        pin_motor_izquierdo_1.off()
        pin_motor_izquierdo_2.on()
        pin_motor_derecho_1.off()
        pin_motor_derecho_2.on()
    else:
        detener_motores()

def controlar_giro(velocidad):
    if velocidad > 0:
        pin_motor_izquierdo_1.off()
        pin_motor_izquierdo_2.on()
        pin_motor_derecho_1.on()
        pin_motor_derecho_2.off()
    elif velocidad < 0:
        pin_motor_izquierdo_1.on()
        pin_motor_izquierdo_2.off()
        pin_motor_derecho_1.off()
        pin_motor_derecho_2.on()
    else:
        detener_motores()

def detener_motores():
    pin_motor_izquierdo_1.off()
    pin_motor_izquierdo_2.off()
    pin_motor_derecho_1.off()
    pin_motor_derecho_2.off()

def actualizar_posicion():
    global posicion_x, posicion_y, angulo_actual, distancia_recorrida_izquierda, distancia_recorrida_derecha
    delta_izquierdo = distancia_recorrida_izquierda
    delta_derecho = distancia_recorrida_derecha
    delta_distancia = (delta_izquierdo + delta_derecho) / 2
    delta_angulo = (delta_derecho - delta_izquierdo) / 20  # Ajustar este valor según la distancia entre las llantas del robot
    angulo_actual += delta_angulo
    posicion_x += delta_distancia * cos(angulo_actual)
    posicion_y += delta_distancia * sin(angulo_actual)

# Ejecución principal del programa
while True:
    # Realizar otras tareas si es necesario
    time.sleep_ms(100)  # Esperar un tiempo para no saturar la CPU

    # Imprimir la posición actual del robot
    print("Posición actual (x, y):", posicion_x, ",", posicion_y)

    # Realizar movimientos del robot
    mover_adelante(20)  # Mover 20 cm hacia adelante
    girar(90)  # Girar 90 grados a la derecha

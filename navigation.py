from machine import Pin
import time

# Configuración de los pines para los encoders
pin_encoder_izquierdo = Pin(36, Pin.IN)
pin_encoder_derecho = Pin(39, Pin.IN)

# Configuración de los pines para el control de los motores
pin_motor_izquierdo_1 = Pin(23, Pin.OUT)
pin_motor_izquierdo_2 = Pin(22, Pin.OUT)
pin_motor_derecho_1 = Pin(3, Pin.OUT)
pin_motor_derecho_2 = Pin(1, Pin.OUT)

# Variables para almacenar el estado anterior de los encoders
estado_anterior_izquierdo = 0
estado_anterior_derecho = 0

# Constantes relacionadas con el encoder
ranuras_por_vuelta = 24
radio_llanta = 3.9  # Radio de la llanta en cm

# Variables para el cálculo de la distancia recorrida
distancia_recorrida_izquierda = 0
distancia_recorrida_derecha = 0

# Variables para el cálculo del giro de los motores
giro_izquierdo = 0
giro_derecho = 0

# Función de interrupción para el encoder izquierdo
def handle_interrupt_izquierdo(pin):
    global estado_anterior_izquierdo, distancia_recorrida_izquierda, giro_izquierdo
    estado_actual_izquierdo = pin.value()
    if estado_actual_izquierdo != estado_anterior_izquierdo:
        distancia_recorrida_izquierda += 2 * 3.1416 * radio_llanta / ranuras_por_vuelta
        if estado_actual_izquierdo == 1:
            giro_izquierdo += 1
        else:
            giro_izquierdo -= 1
    estado_anterior_izquierdo = estado_actual_izquierdo

# Función de interrupción para el encoder derecho
def handle_interrupt_derecho(pin):
    global estado_anterior_derecho, distancia_recorrida_derecha, giro_derecho
    estado_actual_derecho = pin.value()
    if estado_actual_derecho != estado_anterior_derecho:
        distancia_recorrida_derecha += 2 * 3.1416 * radio_llanta / ranuras_por_vuelta
        if estado_actual_derecho == 1:
            giro_derecho += 1
        else:
            giro_derecho -= 1
    estado_anterior_derecho = estado_actual_derecho

# Configurar las interrupciones para los encoders
pin_encoder_izquierdo.irq(handler=handle_interrupt_izquierdo, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
pin_encoder_derecho.irq(handler=handle_interrupt_derecho, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

# Funciones para controlar los movimientos del robot
def mover_adelante():
    pin_motor_izquierdo_1.on()
    pin_motor_izquierdo_2.off()
    pin_motor_derecho_1.on()
    pin_motor_derecho_2.off()

def mover_atras():
    pin_motor_izquierdo_1.off()
    pin_motor_izquierdo_2.on()
    pin_motor_derecho_1.off()
    pin_motor_derecho_2.on()

def girar_izquierda():
    pin_motor_izquierdo_1.off()
    pin_motor_izquierdo_2.on()
    pin_motor_derecho_1.on()
    pin_motor_derecho_2.off()

def girar_derecha():
    pin_motor_izquierdo_1.on()
    pin_motor_izquierdo_2.off()
    pin_motor_derecho_1.off()
    pin_motor_derecho_2.on()

# Ejecución principal del programa
while True:
    # Realizar otras tareas si es necesario
    time.sleep(0.01)  # Esperar un tiempo para no saturar la CPU

    # Imprimir los resultados de los encoders
    print("Distancia recorrida izquierda (encoder):", distancia_recorrida_izquierda, "cm")
    print("Distancia recorrida derecha (encoder):", distancia_recorrida_derecha, "cm")
    print("Giro izquierdo (encoder):", giro_izquierdo)
    print("Giro derecho (encoder):", giro_derecho)

    # Realizar movimientos del robot
    # Aquí puedes agregar la lógica para determinar los movimientos deseados
    # Por ejemplo, puedes utilizar condiciones if-else según las entradas del usuario

    # Ejemplo: Mover hacia adelante durante 1 segundo y luego detenerse
    mover_adelante()
    time.sleep(1)
    pin_motor_izquierdo_1.off()
    pin_motor_izquierdo_2.off()
    pin_motor_derecho_1.off()
    pin_motor_derecho_2.off()

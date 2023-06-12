from machine import Pin
import time
from math import sin, cos
import neopixel

class Robot:
    def __init__(self):
        # Configuración de los pines para los encoders
        self.pin_encoder_izquierdo = Pin(36, Pin.IN)
        self.pin_encoder_derecho = Pin(39, Pin.IN)

        # Configuración de los pines para el control de los motores
        self.pin_motor_izquierdo_1 = Pin(22, Pin.OUT)
        self.pin_motor_izquierdo_2 = Pin(23, Pin.OUT)
        self.pin_motor_derecho_1 = Pin(18, Pin.OUT)
        self.pin_motor_derecho_2 = Pin(19, Pin.OUT)

        # Configuración de los pines de los sensores IR
        self.pin_ir_adelante = Pin(34, Pin.IN)
        self.pin_ir_derecha = Pin(35, Pin.IN)
        self.pin_ir_derecha_inclinado = Pin(32, Pin.IN)
        self.pin_ir_izquierda = Pin(33, Pin.IN)
        self.pin_ir_izquierda_inclinado = Pin(25, Pin.IN)

        # Configuración del neopixel indicador
        self.neo = neopixel.NeoPixel(Pin(27, Pin.OUT), 1)

        # Constantes relacionadas con el encoder
        self.ranuras_por_vuelta = 24
        self.radio_llanta = 3.9  # Radio de la llanta en cm

        # Constantes de control PID
        self.kp = 0.50  # Ganancia proporcional
        self.ki = 0  # Ganancia integral
        self.kd = 0  # Ganancia derivativa

        # Variables de control PID
        self.error_anterior = 0
        self.integral = 0

        # Variables para el control de movimiento
        self.distancia_recorrida_izquierda = 0
        self.distancia_recorrida_derecha = 0
        self.posicion_x = 0  # Posición actual en el eje x del robot
        self.posicion_y = 0  # Posición actual en el eje y del robot
        self.angulo_actual = 0  # Ángulo actual de orientación del robot
        self.estado_anterior_izquierdo = 0
        self.estado_anterior_derecho = 0
        # Configurar las interrupciones para los encoders
        self.pin_encoder_izquierdo.irq(handler=self.handle_interrupt_izquierdo, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
        self.pin_encoder_derecho.irq(handler=self.handle_interrupt_derecho, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
        
    def handle_interrupt_izquierdo(self, pin):
        estado_actual_izquierdo = pin.value()
        if estado_actual_izquierdo != self.estado_anterior_izquierdo:
            self.distancia_recorrida_izquierda += 2 * 3.1416 * self.radio_llanta / self.ranuras_por_vuelta
        self.estado_anterior_izquierdo = estado_actual_izquierdo
    def handle_interrupt_derecho(self, pin):
        estado_actual_derecho = pin.value()
        if estado_actual_derecho != self.estado_anterior_derecho:
            self.distancia_recorrida_derecha += 2 * 3.1416 * self.radio_llanta / self.ranuras_por_vuelta
        self.estado_anterior_derecho = estado_actual_derecho
    def mover_adelante(self, distancia):
        distancia_objetivo = distancia
        distancia_recorrida_inicial_izquierda = self.distancia_recorrida_izquierda
        distancia_recorrida_inicial_derecha = self.distancia_recorrida_derecha
        while (self.distancia_recorrida_izquierda - distancia_recorrida_inicial_izquierda) < distancia_objetivo:
            error = (self.distancia_recorrida_izquierda - distancia_recorrida_inicial_izquierda) - (self.distancia_recorrida_derecha - distancia_recorrida_inicial_derecha)
            velocidad = self.kp * error
            self.controlar_velocidad(velocidad)
            self.actualizar_posicion()
            time.sleep(0.01)
        self.detener_motores()

    def girar(self, angulo):
        angulo_objetivo = angulo
        angulo_inicial = self.angulo_actual
        while abs(self.angulo_actual - angulo_inicial) < angulo_objetivo:
            error = angulo_objetivo - (self.angulo_actual - angulo_inicial)
            velocidad = self.kp * error
            self.controlar_giro(velocidad)
            self.actualizar_posicion()
            time.sleep(0.01)
        self.detener_motores()

    def controlar_velocidad(self, velocidad):
        if velocidad > 0:
            self.pin_motor_izquierdo_1.on()
            self.pin_motor_izquierdo_2.off()
            self.pin_motor_derecho_1.on()
            self.pin_motor_derecho_2.off()
        elif velocidad < 0:
            self.pin_motor_izquierdo_1.off()
            self.pin_motor_izquierdo_2.on()
            self.pin_motor_derecho_1.off()
            self.pin_motor_derecho_2.on()
        else:
            self.detener_motores()

    def controlar_giro(self, velocidad):
        if velocidad > 0:
            self.pin_motor_izquierdo_1.off()
            self.pin_motor_izquierdo_2.on()
            self.pin_motor_derecho_1.on()
            self.pin_motor_derecho_2.off()
        elif velocidad < 0:
            self.pin_motor_izquierdo_1.on()
            self.pin_motor_izquierdo_2.off()
            self.pin_motor_derecho_1.off()
            self.pin_motor_derecho_2.on()
        else:
            self.detener_motores()

    def detener_motores(self):
        self.pin_motor_izquierdo_1.off()
        self.pin_motor_izquierdo_2.off()
        self.pin_motor_derecho_1.off()
        self.pin_motor_derecho_2.off()

    def actualizar_posicion(self):
        print("Distancia recorrida izquierda:", self.distancia_recorrida_izquierda, "cm")
        print("Distancia recorrida derecha:", self.distancia_recorrida_derecha, "cm")

    def ejecutar(self):
        while True:
            # Realizar otras tareas si es necesario
            time.sleep_ms(1000)  # Esperar un tiempo para no saturar la CPU
            # Realizar movimientos del robot
            self.mover_adelante(10)  # Mover 10 cm hacia adelante
            self.girar(90)  # Girar 90 grados a la derecha

robot = Robot()
robot.ejecutar()

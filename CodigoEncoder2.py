from machine import Pin
import time
import math
import neopixel

class Robot:
    def __init__(self):
        # Configuración de los pines para los encoders
        self.pin_encoder_izquierdo = Pin(36, Pin.IN)  # Pin del encoder izquierdo
        self.pin_encoder_derecho = Pin(39, Pin.IN)  # Pin del encoder derecho

        # Configuración de los pines para el control de los motores
        self.pin_motor_izquierdo_1 = Pin(22, Pin.OUT)  # Pin 1 del motor izquierdo
        self.pin_motor_izquierdo_2 = Pin(23, Pin.OUT)  # Pin 2 del motor izquierdo
        self.pin_motor_derecho_1 = Pin(18, Pin.OUT)  # Pin 1 del motor derecho
        self.pin_motor_derecho_2 = Pin(19, Pin.OUT)  # Pin 2 del motor derecho

        # Configuración de los pines de los sensores IR
        self.pin_ir_adelante = Pin(34, Pin.IN)  # Pin del sensor IR hacia adelante
        self.pin_ir_derecha = Pin(35, Pin.IN)  # Pin del sensor IR hacia la derecha
        self.pin_ir_derecha_inclinado = Pin(32, Pin.IN)  # Pin del sensor IR hacia la derecha inclinado
        self.pin_ir_izquierda = Pin(33, Pin.IN)  # Pin del sensor IR hacia la izquierda
        self.pin_ir_izquierda_inclinado = Pin(25, Pin.IN)  # Pin del sensor IR hacia la izquierda inclinado

        # Configuración del neopixel indicador
        self.neo = neopixel.NeoPixel(Pin(27, Pin.OUT), 1)  # Pin del neopixel indicador

        # Constantes relacionadas con el encoder
        self.ranuras_por_vuelta = 24  # Número de ranuras por vuelta del encoder
        self.radio_llanta = 3.9  # Radio de la llanta en cm

        # Constantes de control PID
        self.kp = 1.50  # Ganancia proporcional
        self.ki = 0.6  # Ganancia integral
        self.kd = 0.5  # Ganancia derivativa

        # Variables de control PID
        self.error_anterior = 0  # Valor del error anterior
        self.integral = 0  # Valor de la integral acumulada

        # Variables para el control de movimiento
        self.distancia_recorrida_izquierda = 0  # Distancia recorrida por la rueda izquierda
        self.distancia_recorrida_derecha = 0  # Distancia recorrida por la rueda derecha
        self.angulo_actual = 0  # Ángulo actual de orientación del robot
        self.estado_anterior_izquierdo = 0  # Estado anterior del encoder izquierdo
        self.estado_anterior_derecho = 0  # Estado anterior del encoder derecho
        self.direccion_actual = 'Norte'  # Dirección actual del robot

        # Configurar las interrupciones para los encoders
        self.pin_encoder_izquierdo.irq(handler=self.handle_interrupt_izquierdo, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)  # Configurar interrupción para el encoder izquierdo
        self.pin_encoder_derecho.irq(handler=self.handle_interrupt_derecho, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)  # Configurar interrupción para el encoder derecho

    def handle_interrupt_izquierdo(self, pin):
        estado_actual_izquierdo = pin.value()
        if estado_actual_izquierdo != self.estado_anterior_izquierdo:
            # Actualizar distancia recorrida por la rueda izquierda
            self.distancia_recorrida_izquierda += 2 * 3.1416 * self.radio_llanta / (self.ranuras_por_vuelta * 2)
        self.estado_anterior_izquierdo = estado_actual_izquierdo
        

    def handle_interrupt_derecho(self, pin):
        estado_actual_derecho = pin.value()
        if estado_actual_derecho != self.estado_anterior_derecho:
            # Actualizar distancia recorrida por la rueda derecha
            self.distancia_recorrida_derecha += 2 * 3.1416 * self.radio_llanta / (self.ranuras_por_vuelta * 2)
        self.estado_anterior_derecho = estado_actual_derecho
        

    def detener_motores(self):
        # Detener los motores
        self.pin_motor_izquierdo_1.off()
        self.pin_motor_izquierdo_2.off()
        self.pin_motor_derecho_1.off()
        self.pin_motor_derecho_2.off()

    def controlar_motores(self, velocidad_objetivo):
        # Obtener la velocidad actual de los motores (promedio entre las ruedas izquierda y derecha)
        velocidad_actual = (self.distancia_recorrida_izquierda + self.distancia_recorrida_derecha) / 2

        # Calcular el error entre la velocidad objetivo y la velocidad actual
        error = velocidad_objetivo - velocidad_actual

        # Calcular los componentes proporcional, integral y derivativo
        componente_p = self.kp * error
        self.integral += self.ki * error
        componente_i = self.integral
        componente_d = self.kd * (error - self.error_anterior)

        # Calcular la señal de control total
        senal_control = componente_p + componente_i + componente_d

        # Controlar los motores según la señal de control
        # Aquí debes ajustar los valores de los pines de control de los motores
        # para aumentar o disminuir la velocidad y dirección según la señal de control.

        # Ejemplo:
        if senal_control > 0:
            # Mover hacia adelante
            self.pin_motor_izquierdo_1.on()
            self.pin_motor_izquierdo_2.off()
            self.pin_motor_derecho_1.on()
            self.pin_motor_derecho_2.off()
        else:
            # Mover hacia atrás
            self.pin_motor_izquierdo_1.off()
            self.pin_motor_izquierdo_2.on()
            self.pin_motor_derecho_1.off()
            self.pin_motor_derecho_2.on()

        # Almacenar el valor del error actual para la próxima iteración
        self.error_anterior = error

    # Resto de métodos del Robot (mover_adelante, girar, detener_motores, etc.)
    def distancia_recorrida_promedio(self):
        # Calcular la distancia recorrida promedio entre las ruedas izquierda y derecha
        return (self.distancia_recorrida_izquierda + self.distancia_recorrida_derecha) / 2

    def mover_adelante(self, distancia):
        # Reiniciar las distancias recorridas por las ruedas izquierda y derecha
        self.distancia_recorrida_izquierda = 0
        self.distancia_recorrida_derecha = 0

        # Calcular el número de ranuras que deben pasar los encoders
        ranuras_objetivo = (distancia * self.ranuras_por_vuelta) / (2 * 3.1416 * self.radio_llanta)

        # Controlar los motores para mover el robot hacia adelante hasta alcanzar la distancia objetivo
        while self.distancia_recorrida_promedio() < ranuras_objetivo:
            self.controlar_motores(1)  # Velocidad objetivo: 1 cm/s

        # Detener los motores una vez que se alcanza la distancia objetivo
        self.detener_motores()
        print("Distancia recorrida izquierda:", self.distancia_recorrida_izquierda, "cm")
        print("Distancia recorrida derecha:", self.distancia_recorrida_derecha, "cm")
        self.distancia_recorrida_izquierda = 0
        self.distancia_recorrida_derecha = 0
        
        
    def controlar_giro(self, angulo_objetivo):
        # Calcular el error entre el ángulo objetivo y el ángulo actual
        error = angulo_objetivo - self.angulo_actual
        
        # Ajustar el error al rango [-180, 180]
        if error > 180:
            error -= 360
        elif error < -180:
            error += 360
        
        # Calcular los componentes proporcional, integral y derivativo
        componente_p = self.kp * error
        self.integral += self.ki * error
        componente_i = self.integral
        componente_d = self.kd * (error - self.error_anterior)
        
        # Calcular la señal de control total
        senal_control = componente_p + componente_i + componente_d
        
        # Controlar los motores según la señal de control
        if senal_control > 0:
            # Girar a la derecha
            self.pin_motor_izquierdo_1.on()
            self.pin_motor_izquierdo_2.off()
            self.pin_motor_derecho_1.off()
            self.pin_motor_derecho_2.on()
        else:
            # Girar a la izquierda
            self.pin_motor_izquierdo_1.off()
            self.pin_motor_izquierdo_2.on()
            self.pin_motor_derecho_1.on()
            self.pin_motor_derecho_2.off()
        
        # Almacenar el valor del error actual para la próxima iteración
        self.error_anterior = error
        
    def girar(self, angulo):
        # Actualizar el ángulo actual de orientación del robot
        self.angulo_actual += angulo

        # Ajustar el ángulo actual al rango [0, 360]
        self.angulo_actual %= 360

        # Controlar el giro utilizando el controlador PID
        self.integral = 0  # Reiniciar la integral acumulada
        self.error_anterior = 0  # Reiniciar el error anterior
        
        angulo_objetivo = self.angulo_actual + angulo
        angulo_objetivo %= 360
        
        while abs(self.angulo_actual - angulo_objetivo) > 1:
            self.controlar_giro(angulo_objetivo)
            time.sleep(0.01)  # Pequeña pausa para no saturar la CPU
        
        # Detener los motores una vez completado el giro
        self.detener_motores()
        
        def obtener_direccion(self):
            # Definir los rangos de ángulos para cada dirección cardinal
            rangos = [ (-45, 45, "Norte"),
                (45, 135, "Este"),
                (135, 225, "Sur"),
                (225, 315, "Oeste"),
                (315, 405, "Norte")]
            
            # Obtener el ángulo actual ajustado al rango [0, 360]
            angulo_ajustado = self.angulo_actual % 360
            
            # Buscar la dirección correspondiente al ángulo actual
            for rango in rangos:
                if rango[0] <= angulo_ajustado < rango[1]:
                    return rango[2]
            
            # Si no se encuentra ninguna dirección, devolver 'Desconocida'
            return 'Desconocida'
        
        
    def ejecutar(self):
        while True:
        
            # Realizar otras tareas si es necesario
            time.sleep_ms(4000)  # Esperar un tiempo para no saturar la CPU
            # Realizar movimientos del robot
            self.mover_adelante(20)  # Mover 10 cm hacia adelante
            
            time.sleep_ms(2000)  # Esperar un tiempo para no saturar la CPU
            self.girar(90)  # Girar 90 grados a la derecha
            print("------------------------")
            
            
# Crear una instancia del robot y ejecutarlo
robot = Robot()
direccion_actual = robot.obtener_direccion()
print(direccion_actual)  # Esto imprimirá 'Este' si el punto inicial es 'Norte'
robot.ejecutar()


# Importar módulos y bibliotecas
from dcmotor import DCMotor
from encode import Encoder

# Definir la clase Navigation
class Navigation(object):
    def __init__(self, direction):
        self.direction = direction
        self.motors = DCMotor(1, 2, 3, 4)  # Crear una instancia de DCMotor con los pines especificados
        self.encoder = Encoder(7)  # Crear una instancia de Encoder con el pin especificado

    def forward(self):
        counter_pulse = 0
        pulse_movement = 255  # Define el número de pulsos para avanzar
        while counter_pulse < pulse_movement:
            self.motors.forward()  # Mover los motores hacia adelante
        self.motors.stop()  # Detener los motores

    def backward(self):
        counter_pulse = 0
        pulse_movement = 255  # Define el número de pulsos para retroceder
        while counter_pulse < pulse_movement:
            self.motors.backward()  # Mover los motores hacia atrás
        self.motors.stop()  # Detener los motores

    def turn_right(self):
        counter_pulse = 0
        pulse_movement = 100  # Define el número de pulsos para girar a la derecha
        while counter_pulse < pulse_movement:
            self.motors.turn_rigth()  # Girar hacia la derecha moviendo los motores hacia adelante
        self.motors.stop()  # Detener los motores

    def turn_left(self):
        counter_pulse = 0
        pulse_movement = 100  # Define el número de pulsos para girar a la izquierda
        while counter_pulse < pulse_movement:
            self.motors.turn_left()  # Girar hacia la izquierda moviendo los motores hacia atrás
        self.motors.stop()  # Detener los motores

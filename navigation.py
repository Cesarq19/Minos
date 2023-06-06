# Import modules and libraries
from dcmotor import DCMotor
from encode import Encoder


class Navigation(object):
    def __init__(self, direction):
        self.direction = direction
        self.motors = DCMotor(1, 2, 3, 4)
        self.encoder = Encoder(7)

    def forward(self):
        counter_pulse = 0
        pulse_movement = 255
        while counter_pulse < pulse_movement:
            self.motors.forward()
        self.motors.stop()

    def backward(self):
        counter_pulse = 0
        pulse_movement = 255
        while counter_pulse < pulse_movement:
            self.motors.backward()
        self.motors.stop()

    def turn_right(self):
        pass

    def turn_left(self):
        pass

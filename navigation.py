# Import modules and libraries
from dcmotor import DCMotor
from encode import Encoder

class Navigation(object):
    def __init__(self, direction):
        self.direction = direction
        self.motors = DCMotor(1, 2, 3, 4)
        self.encoder = Encoder(7)

    def forward(self):
        pass
    def backward(self):
        pass
    def turn_right(self):
        pass
    def turn_left(self):
        pass

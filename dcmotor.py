# Import modules and libraries
from machine import Pin


# Define the object Motor
class DCMotor(object):
    def __init__(self, in1, in2, in3, in4):
        self.in1 = Pin(in1)
        self.in2 = Pin(in2)
        self.in3 = Pin(in3)
        self.in4 = Pin(in4)

    def forward(self):
        self.in1.value(1)
        self.in2.value(0)
        self.in3.value(1)
        self.in4.value(0)
        print("forward")

    def backward(self):
        self.in1.value(0)
        self.in2.value(1)
        self.in3.value(0)
        self.in4.value(1)
        print("backward")

    def turn_right(self):
        self.in1.value(0)
        self.in2.value(1)
        self.in3.value(1)
        self.in4.value(0)
        print("right")

    def turn_left(self):
        self.in1.value(1)
        self.in2.value(0)
        self.in3.value(0)
        self.in4.value(1)
        print("left")

    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.in3.value(0)
        self.in4.value(0)
        print("stop")

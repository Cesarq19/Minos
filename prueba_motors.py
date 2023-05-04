from dcmtor import DCMotor       
from machine import Pin, PWM   
from time import sleep_ms   
from mpu6050 import MPU6050

class Robot:
    def __init__(self, pin1_left, pin2_left, enable_left, pin1_right, pin2_right, enable_right, min_duty=750, max_duty=1023):
        self.left_motor = DCMotor(pin1_left, pin2_left, enable_left, min_duty, max_duty)
        self.right_motor = DCMotor(pin1_right, pin2_right, enable_right, min_duty, max_duty)
        self.mpu = MPU6050(14, 13)
        self.mpu.MPU_Init()
        self.G = 9.8
        
    def forward(self, speed):
        self.left_motor.forward(speed)
        self.right_motor.forward(speed)
    
    def backwards(self, speed):
        self.left_motor.backwards(speed)
        self.right_motor.backwards(speed)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
    def turn_left(self, speed, degrees):
        self.mpu.reset_angle()
        self.right_motor.forward(speed)
        while abs(self.mpu.get_angle()) < degrees:
            self.left_motor.backwards()
        self.stop()
            
    def turn_right(self, speed, degrees):
        self.mpu.reset_angle()
        self.left_motor.forward(speed)
        while abs(self.mpu.get_angle()) < degrees:
            self.right_motor.backwards()
        self.stop()

# Ejemplo de uso
frequency = 15000
left_pin1 = Pin(2, Pin.OUT)
left_pin2 = Pin(15, Pin.OUT)
left_enable = PWM(Pin(13), frequency)
right_pin1 = Pin(4, Pin.OUT)
right_pin2 = Pin(16, Pin.OUT)
right_enable = PWM(Pin(14), frequency)

robot = Robot(left_pin1, left_pin2, left_enable, right_pin1, right_pin2, right_enable, 350, 1023)

robot.forward(50)
sleep_ms(10000)
robot.stop()
sleep_ms(10000)
robot.backwards(100)
sleep_ms(10000)
robot.forward(60)
sleep_ms(10000)

# Girar a la izquierda con una velocidad de 50 y un ángulo de 90 grados
robot.turn_left(50, 90)

# Girar a la derecha con una velocidad de 50 y un ángulo de 90 grados
robot.turn_right(50, 90)

from dcmtor2 import DCMotor       
from machine import Pin, PWM   
from time import sleep_ms   
from mpu6050 import MPU6050


# Ejemplo de uso

frequency = 10000
left_pin1 = Pin(2, Pin.OUT)
left_pin2 = Pin(15, Pin.OUT)
left_enable = PWM(Pin(22), frequency)
right_pin1 = Pin(4, Pin.OUT)
right_pin2 = Pin(18, Pin.OUT)
right_enable = PWM(Pin(21), frequency)

robot =DCMotor(left_pin1, left_pin2,right_pin1, right_pin2,left_enable,right_enable, 350, 1023)

robot.forward(50)
sleep_ms(3000)
robot.stop()
sleep_ms(1000)
robot.backward(50)
sleep_ms(3000)
robot.stop()
sleep_ms(1000)
robot.turn_right(50)
sleep_ms(3000)
robot.stop()
sleep_ms(3000)
robot.turn_left(40)
sleep_ms(3000)
robot.stop()

# Girar a la izquierda con una velocidad de 50 y un ángulo de 90 grados
#robot.turn_left(50, 90)


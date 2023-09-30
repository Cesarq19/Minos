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
sleep_ms(5000)
robot.stop()
sleep_ms(3000)
robot.backward(100)
sleep_ms(4000)
robot.stop()
sleep_ms(3000)
robot.forward(60)
sleep_ms(5000)
robot.stop()
sleep_ms(2000)
robot.turn_right(30)
sleep_ms(1000)
robot.stop()
sleep_ms(3000)
robot.turn_left(100)
sleep_ms(1000)
robot.stop()

# Girar a la izquierda con una velocidad de 50 y un ángulo de 90 grados
#robot.turn_left(50, 90)

# Girar a la derecha con una velocidad de 50 y un ángulo de 90 grados
#robot.turn_right(50, 90)

# Import necessary libraries
from machine import Pin
import time

# Define infrared sensor pins
LEFT_SENSOR_PIN = 12
FRONT_SENSOR_PIN = 14
RIGHT_SENSOR_PIN = 27
LEFT_45_SENSOR_PIN = 33
RIGHT_45_SENSOR_PIN = 32

# Initialize infrared sensor pins as input pins
left_sensor = Pin(LEFT_SENSOR_PIN, Pin.IN)
front_sensor = Pin(FRONT_SENSOR_PIN, Pin.IN)
right_sensor = Pin(RIGHT_SENSOR_PIN, Pin.IN)
left_45_sensor = Pin(LEFT_45_SENSOR_PIN, Pin.IN)
right_45_sensor = Pin(RIGHT_45_SENSOR_PIN, Pin.IN)
def sensar_paredes(direccion, position):
    left_value = left_sensor.value()
    front_value = front_sensor.value()
    right_value = right_sensor.value()
    return left_value,front_value,right_value


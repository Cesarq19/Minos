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

# Define function to check if a cell is accessible
def is_accessible():
    left_value = left_sensor.value()
    front_value = front_sensor.value()
    right_value = right_sensor.value()
    left_45_value = left_45_sensor.value()
    right_45_value = right_45_sensor.value()

    # Check if there is a wall or obstacle in the way
    if left_value and front_value and right_value:
        return False
    if left_45_value and front_value:
        return False
    if right_45_value and front_value:
        return False

    # Otherwise, the cell is accessible
    return True

# Example usage
if is_accessible():
    print("Cell is accessible")
else:
    print("Cell is blocked")

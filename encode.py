# Import modules
from machine import Pin
class Encoder(object):
    def __init__(self, data: int=3, resolution: int=3600):
        self.data = Pin(data, Pin.IN)
        self.resolution = resolution

    def count(self):
        pass

    def gyro_count(self):
        pass
    
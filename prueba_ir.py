# Import necessary libraries
from machine import Pin
from time import sleep_ms   
from flood_fill_algo import flood_fill

algoritmo=flood_fill()
algoritmo.flood_fill_llenado(3,2)
print(algoritmo.maze_hwalls)
print(algoritmo.maze_vwalls)
print(algoritmo.maze_weights)
position =(4,0)#tengo la position del carro
direccion=0 #obtengo la direccion del carro 
# Define infrared sensor pins
LEFT_SENSOR_PIN = 33
FRONT_SENSOR_PIN = 34
RIGHT_SENSOR_PIN = 35
# LEFT_45_SENSOR_PIN = 33
# RIGHT_45_SENSOR_PIN = 32

# Initialize infrared sensor pins as input pins
left_sensor = Pin(LEFT_SENSOR_PIN, Pin.IN)
front_sensor = Pin(FRONT_SENSOR_PIN, Pin.IN)
right_sensor = Pin(RIGHT_SENSOR_PIN, Pin.IN)
#left_45_sensor = Pin(LEFT_45_SENSOR_PIN, Pin.IN)
#right_45_sensor = Pin(RIGHT_45_SENSOR_PIN, Pin.IN)
# def sensar_paredes(direccion, position):
#    left_value = left_sensor.value()
#    front_value = front_sensor.value()
#    right_value = right_sensor.value()
#    return left_value,front_value,right_value
def actualizar_paredes():
    """esta funcion verifica las paredes y las almacena en las matrices de paredes"""

    if not (front_sensor and right_sensor and left_sensor):#si no encuentra ninguna pared no hace nada 
        pass
    elif position=="sur"and (front_sensor or right_sensor or left_sensor):
        #verifico que no haya valores en la matriz 
        if algoritmo.maze_hwalls[position[0],position[1]]==0 and algoritmo.maze_vwalls[position[0],position[1]]==0:
            if front_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=2
            if right_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=1
            if left_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=2
            if right_sensor and left_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=3
    elif position=="oeste"and (front_sensor or right_sensor or left_sensor):
        if algoritmo.maze_hwalls[position[0],position[1]]==0 and algoritmo.maze_vwalls[position[0],position[1]]==0:
            if front_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=1
            if right_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=1
            if left_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=2
            if right_sensor and left_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=3
    elif position=="norte"and (front_sensor or right_sensor or left_sensor):
        if algoritmo.maze_hwalls[position[0],position[1]]==0 and algoritmo.maze_vwalls[position[0],position[1]]==0:
            if front_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=1
            if right_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=2
            if left_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=1
            if right_sensor and left_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=3
    elif position=="este"and (front_sensor or right_sensor or left_sensor):
        if algoritmo.maze_hwalls[position[0],position[1]]==0 and algoritmo.maze_vwalls[position[0],position[1]]==0:
            if front_sensor:
                algoritmo.maze_vwalls[position[0],position[1]]=2
            if right_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=2
            if left_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=1
            if right_sensor and left_sensor:
                algoritmo.maze_hwalls[position[0],position[1]]=3


print(f"sendor frente :{front_sensor.value()}")
print(f"sendor derecha :{right_sensor.value()}")
print(f"sendor izquierda :{left_sensor.value()}")
actualizar_paredes()
print(algoritmo.maze_vwalls)
print(algoritmo.maze_hwalls)

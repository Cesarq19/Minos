# Import necessary libraries
from machine import Pin
from time import sleep_ms   
from flood_fill_algo import flood_fill

algoritmo=flood_fill()
algoritmo.flood_fill_llenado(3,2)
print(algoritmo.maze_hwalls)
print(algoritmo.maze_vwalls)
print(algoritmo.maze_weights)
position=[4,0]#tengo la position del carro

direccion=0 #obtengo la direccion del carro 
# Define infrared sensor pins
left_value_PIN = 33
front_value_PIN = 34
right_value_PIN = 35
# LEFT_45_SENSOR_PIN = 33
# RIGHT_45_SENSOR_PIN = 32

# Initialize infrared sensor pins as input pins
left_sensor = Pin(left_value_PIN, Pin.IN)
front_sensor = Pin(front_value_PIN, Pin.IN)
right_sensor = Pin(right_value_PIN, Pin.IN)

#prueba
# left_value=0
# front_value=1
# right_value=0

#left_45_sensor = Pin(LEFT_45_SENSOR_PIN, Pin.IN)
#right_45_sensor = Pin(RIGHT_45_SENSOR_PIN, Pin.IN)
def sensar_paredes():
    left_value = left_sensor.value()
    front_value = front_sensor.value()
    right_value = right_sensor.value()
    return left_value,front_value,right_value
def actualizar_paredes(position_x,position_y,direccion):
    """esta funcion verifica las paredes y las almacena en las matrices de paredes"""
    left_value,front_value,right_value=sensar_paredes()
    if front_value and  right_value and left_value:#si no encuentra ninguna pared no hace nada
        print("pasa")
        pass
    elif algoritmo.maze_hwalls[position_x][position_y]==0 or algoritmo.maze_vwalls[position_x][position_y]==0:
        print("prueba")
        if direccion==180 and (not front_value or not right_value or not left_value):
            #verifico que no haya valores en la matriz
                if not front_value:
                    algoritmo.maze_hwalls[position_x][position_y]=2
                if not right_value:
                    algoritmo.maze_vwalls[position_x][position_y]=1
                if not left_value:
                    algoritmo.maze_vwalls[position_x][position_y]=2
                if not right_value and not left_value:
                    algoritmo.maze_vwalls[position_x][position_y]=3
        elif direccion==270 and (not front_value or not right_value or not left_value):
                if not front_value:
                    algoritmo.maze_vwalls[position_x][position_y]=1
                if not right_value:
                    algoritmo.maze_hwalls[position_x][position_y]=1
                if not left_value:
                    algoritmo.maze_hwalls[position_x][position_y]=2
                if not right_value and not left_value:
                    algoritmo.maze_hwalls[position_x][position_y]=3
        elif direccion==0 and (not front_value or not right_value or not left_value):
                print("hola")
                if not front_value:
                    algoritmo.maze_hwalls[position_x][position_y]=1
                if not right_value:
                    algoritmo.maze_vwalls[position_x][position_y]=2
                if not left_value:
                    algoritmo.maze_vwalls[position_x][position_y]=1
                if not right_value and not left_value:
                    algoritmo.maze_vwalls[position_x][position_y]=3
        elif direccion==90 and (not front_value or not right_value or not left_value):
                if not front_value:
                    algoritmo.maze_vwalls[position_x][position_y]=2
                if not right_value:
                    algoritmo.maze_hwalls[position_x][position_y]=2
                if not left_value:
                    algoritmo.maze_hwalls[position_x][position_y]=1
                if not right_value and not left_value:
                    algoritmo.maze_hwalls[position_x][position_y]=3

def siguiente_posicion(posicion,orientacion):
    """"la funcion obtiene la siguiente posicion y la orientacion a la que debe esta el carro """
    avances=[]
    orientacion_siguiete=orientacion
    celda_siguiente=(0,0)
    #dependiendo de la direccion seleccionamos el sentido que vamos a verificar las celdas 
    if direccion==0:
        avances=[(-1,0),(0,1),(1,0),(0,-1)]
    elif direccion==90:
        avances=[(0,1),(1,0),(0,-1),(-1,0)]
    elif direccion==180:
        avances=[(1,0),(0,-1),(-1,0),(0,1)]
    elif direccion==270:
        avances=[(0,-1),(-1,0),(0,1),(1,0)]
    for avance in avances:
        #obtenemos las posiciones de avance 
        nx,ny=posicion[0]+avance[0],posicion[1]+avance[1]
        if orientacion_siguiete>270:
            orientacion_siguiete=0
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        elif algoritmo.maze_weights[nx][ny]==(algoritmo.maze_weights[posicion[0]][posicion[1]]-1):
            celda_siguiente=(nx,ny)
            break
        orientacion_siguiete+=90#aumentamos la orientacion 
    return celda_siguiente,orientacion_siguiete

print(f"sendor frente :{front_sensor.value()}")
print(f"sendor derecha :{right_sensor.value()}")
print(f"sendor izquierda :{left_sensor.value()}")
actualizar_paredes(position[0],position[1],direccion)
celda_siguiente,siguiente_orientacion=siguiente_posicion(position,direccion)
print(algoritmo.maze_vwalls)
print(algoritmo.maze_hwalls)
print(f"celda siguiente :{celda_siguiente} orientacion siguiente: {siguiente_orientacion}")



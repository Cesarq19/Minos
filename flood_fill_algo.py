import numpy as np 
# Define the dimensions of the maze
MAZE_WIDTH = 10
MAZE_HEIGHT = 10

# Define the cell size in centimeters
CELL_SIZE = 20

# Define the initial cell values
maze_weights = np.zeros((MAZE_HEIGHT,MAZE_WIDTH))
maze_vwalls = np.zeros((MAZE_HEIGHT,MAZE_WIDTH))
maze_hwalls = np.zeros((MAZE_HEIGHT,MAZE_WIDTH))
#para las matrices vwalls 1| |2 ,ambas es 3
#para la matriz hwals 1- 2_ , ambas es 3


print(maze_hwalls)
print(maze_vwalls)
def verificar_celdas_vecinas(valores_celdas,peso_celda,comienzo_x,comienzo_y):#valores celdas son los valores del queue
    """ verifica las celdas vecinas tomando en cuenta los valores de las pareces para almacenar el peso correspondiente"""
    new_queue=[]
    for posx,posy in valores_celdas:
        for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:
            nx,ny=posx+dx,posy+dy
            #nx fila ,ny columna 
            # Check if the neighbor cell is within the maze bounds
            if nx < 0 or nx >= MAZE_WIDTH or ny < 0 or ny >= MAZE_HEIGHT:
                continue
            # Check if there is a wall between the current cell and the neighbor cell
            #verifica la celda de derecha
            if dx == 0 and dy==1 and(maze_vwalls[nx][ny] == 1 or maze_vwalls[nx][ny] == 3) :
                continue
            #verifica la celda de izquierda
            elif dx == 0 and dy==-1 and (maze_vwalls[nx][ny] == 2 or maze_vwalls[nx][ny] == 3):
                continue
            #verifica la celda de la abajo
            elif dy == 0 and dx==1 and (maze_hwalls[nx][ny] ==1 or maze_hwalls[nx][ny] == 3):
                continue
            #verifica la celda de la arriba
            elif dy == 0 and dx==-1 and (maze_hwalls[nx][ny] == 2 or maze_hwalls[nx][ny] == 3):
                continue

            if not(nx==comienzo_x and ny==comienzo_y) and maze_weights[nx][ny]==0:
                maze_weights[nx][ny]=peso_celda
                new_queue.append((nx,ny))
    return new_queue

def flood_fill(start_x,start_y):
    """realiza el calculo de los pesos de las celdas usando  el flood fill algorithm """
    queue=[(start_x,start_y)]#almacenasmos los valores con el que comienza en el queue
    peso=1#determinamos un peso inicial para dar referencia al inicio
    print(queue)
    terminaor=True#definimos un terminador del bucle cuando termine todos los pesos en las celdas
    while terminaor:
        queue=verificar_celdas_vecinas(queue,peso,start_x,start_y)
        peso+=1
        if len(queue)==0:
            terminaor=False

# Call the flood fill function with the starting cell coordinates
flood_fill(5, 6)
print(maze_weights)
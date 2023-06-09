#import ulab 
# Define the dimensions of the maze
MAZE_WIDTH = 5
MAZE_HEIGHT = 5

# Define the cell size in centimeters
CELL_SIZE = 20

# Define the initial cell values
#maze_weights = ulab.numpy.zeros((MAZE_HEIGHT,MAZE_WIDTH))
#maze_vwalls = ulab.numpy.zeros((MAZE_HEIGHT,MAZE_WIDTH))
#maze_hwalls = ulab.numpy.zeros((MAZE_HEIGHT,MAZE_WIDTH))
#prueba con listas

def llenado(fila,columna):
    matriz=[]
    for i in range(fila):
        matriz.append([])
        for j in range(columna):
            matriz[i].append(0)
    return matriz
maze_weights =llenado(MAZE_HEIGHT,MAZE_WIDTH)
maze_vwalls = llenado(MAZE_HEIGHT,MAZE_WIDTH)
maze_hwalls = llenado(MAZE_HEIGHT,MAZE_WIDTH)
#para las matrices vwalls 1| |2 ,ambas es 3
#para la matriz hwals 1- 2_ , ambas es 3
class flood_fill():
    def __init__(self) :
        self.maze_weights=maze_weights
        self.maze_vwalls=maze_vwalls
        self.maze_hwalls=maze_hwalls

    # print(maze_hwalls)
    # print(maze_vwalls)
    def verificar_celdas_vecinas(self,valores_celdas,peso_celda,comienzo_x,comienzo_y):#valores celdas son los valores del queue
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
                if dx == 0 and dy==1 and(self.maze_vwalls[nx][ny] == 1 or self.maze_vwalls[nx][ny] == 3) :
                    continue
                #verifica la celda de izquierda
                elif dx == 0 and dy==-1 and (self.maze_vwalls[nx][ny] == 2 or self.maze_vwalls[nx][ny] == 3):
                    continue
                #verifica la celda de la abajo
                elif dy == 0 and dx==1 and (self.maze_hwalls[nx][ny] ==1 or self.maze_hwalls[nx][ny] == 3):
                    continue
                #verifica la celda de la arriba
                elif dy == 0 and dx==-1 and (self.maze_hwalls[nx][ny] == 2 or self.maze_hwalls[nx][ny] == 3):
                    continue

                if not(nx==comienzo_x and ny==comienzo_y) and self.maze_weights[nx][ny]==0:
                    self.maze_weights[nx][ny]=peso_celda
                    new_queue.append((nx,ny))
        return new_queue

    def flood_fill_llenado(self,start_x,start_y):
        """realiza el calculo de los pesos de las celdas usando  el flood fill algorithm , tomando como datos
        start_x y start_y que es la ubicacion de la meta"""
        queue=[(start_x,start_y)]#almacenasmos los valores con el que comienza en el queue
        self.maze_weights=llenado(MAZE_HEIGHT,MAZE_WIDTH)
        peso=1#determinamos un peso inicial para dar referencia al inicio
        print(queue)
        terminator=True#definimos un terminador del bucle cuando termine todos los pesos en las celdas
        while terminator:
            queue=self.verificar_celdas_vecinas(queue,peso,start_x,start_y)
            peso+=1
            if len(queue)==0:
                terminator=False

# Call the flood fill function with the starting cell coordinates
# flood_fill(5, 6)
# print(self.maze_weights)
#algoritmo=flood_fill()
#algoritmo.flood_fill_llenado(3,2)
#print(algoritmo.maze_weights)
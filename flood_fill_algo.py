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
print(maze_weights)
print(maze_vwalls)
print(maze_hwalls)

def verificar_celdas_vecinas(valores_celdas,peso_celda):
    new_queue=[]
    for posx,posy in valores_celdas:
        for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:
            nx,ny=posx+dx,posy+dy
            # Check if the neighbor cell is within the maze bounds
            if nx < 0 or nx >= MAZE_WIDTH-1 or ny < 0 or ny >= MAZE_HEIGHT-1:
                continue
            # Check if there is a wall between the current cell and the neighbor cell
            
            if dx == 0 and dy==1 and maze_vwalls[nx][ny] == 2:#verif
                continue
            elif dx == 0 and dy==-1 and maze_vwalls[nx][ny] == 1:
                continue
            elif dy == 0 and dx==1 and maze_hwalls[nx][ny] ==1:
                continue
            elif dy == 0 and dx==-1 and maze_hwalls[nx][ny] == 2:
                continue

            if not(nx==4 and ny==4) and maze_weights[nx][ny]==0:
                maze_weights[nx][ny]=peso_celda
                new_queue.append((nx,ny))
    return new_queue

def flood_fill(start_x,start_y):
    queue=[(start_x,start_y)]
    peso=1
    print(queue)
    # while True:
    #     x, y = queue.pop(0)
    #     pass

# Define the flood fill function
# def flood_fill(start_x, start_y):
#     # Set the goal cell value to 0 and add it to the queue
#     maze_weights[start_x][start_y] = 0
#     queue = [(start_x, start_y)]

#     # Process the queue
#     while queue:
#         # Take the front cell in the queue "out of line" for consideration
#         x, y = queue.pop(0)#valores del indice del valor 
#         cell_weight = maze_weights[x][y]

#         # Check all the blank and accessible neighbors of the front cell
#         for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
#             nx, ny = x + dx, y + dy

#             # Check if the neighbor cell is within the maze bounds
#             if nx < 0 or nx >= MAZE_WIDTH or ny < 0 or ny >= MAZE_HEIGHT:
#                 continue

#             # Check if there is a wall between the current cell and the neighbor cell
#             if dx == 0 and maze_vwalls[x][y+dy] != 0:
#                 continue
#             elif dy == 0 and maze_hwalls[x+dx][y] != 0:
#                 continue

#             # Calculate the weight of the neighbor cell
#             if dx == 0:
#                 weight = cell_weight + CELL_SIZE + maze_hwalls[x][y]
#             else:
#                 weight = cell_weight + CELL_SIZE + maze_vwalls[x][y]

#             # Check if the neighbor cell is blank or has a higher weight than the calculated weight
#             if maze_weights[nx][ny] == -1 or maze_weights[nx][ny] > weight:
#                 # Set the neighbor cell weight to the calculated weight
#                 maze_weights[nx][ny] = weight

#                 # Add the processed cell to the queue
#                 queue.append((nx, ny))

# Call the flood fill function with the starting cell coordinates
flood_fill(4,4)
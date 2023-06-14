
from flood_fill_algo import flood_fill
algoritmo=flood_fill()
algoritmo.flood_fill_llenado(3,2)
print(algoritmo.maze_hwalls)
print(algoritmo.maze_vwalls)
print(algoritmo.maze_weights)
position =(4,0)#tengo la position del carro
direccion=0 #obtengo la direccion del carro 
recorrido=[]#donde #se almacena el recorrido 
recorrido.append(position)#almaceno la posiicion
flood_fill(4,4)#genero los pesos

frente,derecha,izquierda=sensar_paredes()
def actualizar_paredes():
    """esta funcion verifica las paredes y las almacena en las matrices de paredes"""

    if not (frente and derecha and izquierda):#si no encuentra ninguna pared no hace nada 
        pass
    elif position=="sur"and (frente or derecha or izquierda):
        #verifico que no haya valores en la matriz 
        if maze_hwalls[position[0],position[1]]!=0 and maze_vwalls[position[0],position[1]]!=0:
            if frente:
                maze_hwalls[position[0],position[1]]=2
            if derecha:
                maze_vwalls[position[0],position[1]]=1
            if izquierda:
                maze_vwalls[position[0],position[1]]=2
            if derecha and izquierda:
                maze_vwalls[position[0],position[1]]=3
    elif position=="oeste"and (frente or derecha or izquierda):
        if maze_hwalls[position[0],position[1]]!=0 and maze_vwalls[position[0],position[1]]!=0:
            if frente:
                maze_vwalls[position[0],position[1]]=1
            if derecha:
                maze_hwalls[position[0],position[1]]=1
            if izquierda:
                maze_hwalls[position[0],position[1]]=2
            if derecha and izquierda:
                maze_hwalls[position[0],position[1]]=3
    elif position=="norte"and (frente or derecha or izquierda):
        if maze_hwalls[position[0],position[1]]!=0 and maze_vwalls[position[0],position[1]]!=0:
            if frente:
                maze_hwalls[position[0],position[1]]=1
            if derecha:
                maze_vwalls[position[0],position[1]]=2
            if izquierda:
                maze_vwalls[position[0],position[1]]=1
            if derecha and izquierda:
                maze_vwalls[position[0],position[1]]=3
    elif position=="este"and (frente or derecha or izquierda):
        if maze_hwalls[position[0],position[1]]!=0 and maze_vwalls[position[0],position[1]]!=0:
            if frente:
                maze_vwalls[position[0],position[1]]=2
            if derecha:
                maze_hwalls[position[0],position[1]]=2
            if izquierda:
                maze_hwalls[position[0],position[1]]=1
            if derecha and izquierda:
                maze_hwalls[position[0],position[1]]=3

def siguiente_posicion():
    """"la funcion obtiene la siguiente posicion y la orientacion a la que debe esta el carro """
    avances=[]
    orientacion_siguiete=direccion
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
        nx,ny=position[0]+avance[0],position[1]+avance[1]
        orientacion_siguiete+=90#aumentamos la orientacion 
        if orientacion_siguiete>270:
            orientacion_siguiete=0
        if matriz_pesos[nx][ny]==(matriz_pesos[nx][ny]+1):
            celda_siguiente=(nx,ny)
            break
    return celda_siguiente,orientacion_siguiete

angulo_giro=orientacion_siguiente-direccion_actual
girar(angulo_giro)
if frente==1:
    avanzar()
    posicion=celda_siguiente
    

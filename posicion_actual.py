position =(4,0)#tengo la position del carro
direccion="norte"#obtengo la direccion del carro 
recorrido=[]#donde #se almacena el recorrido 
recorrido.append(position)#almaceno la posiicion
flood_fill(4,4)#genero los pesos
matriz_pesos=maze_weights
frente,derecha,izquierda=sensar_paredes()
def actualizar_paredes():
    """esta funcion verifica las paredes y las almacena en las matrices de paredes"""
    if not (frente and derecha and izquierda):#si no encuentra ninguna pared no hace nada 
        pass
    elif position=="sur"and (frente or derecha or izquierda):
        if frente:
            maze_hwalls[position[0],position[1]]=2
        if derecha:
            maze_vwalls[position[0],position[1]]=1
        if izquierda:
            maze_vwalls[position[0],position[1]]=2
        if derecha and izquierda:
            maze_vwalls[position[0],position[1]]=3
    elif position=="oeste"and (frente or derecha or izquierda):
        if frente:
            maze_vwalls[position[0],position[1]]=1
        if derecha:
            maze_hwalls[position[0],position[1]]=1
        if izquierda:
            maze_hwalls[position[0],position[1]]=2
        if derecha and izquierda:
            maze_hwalls[position[0],position[1]]=3
    elif position=="norte"and (frente or derecha or izquierda):
        if frente:
            maze_hwalls[position[0],position[1]]=1
        if derecha:
            maze_vwalls[position[0],position[1]]=2
        if izquierda:
            maze_vwalls[position[0],position[1]]=1
        if derecha and izquierda:
            maze_vwalls[position[0],position[1]]=3
    elif position=="este"and (frente or derecha or izquierda):
        if frente:
            maze_vwalls[position[0],position[1]]=2
        if derecha:
            maze_hwalls[position[0],position[1]]=2
        if izquierda:
            maze_hwalls[position[0],position[1]]=1
        if derecha and izquierda:
            maze_hwalls[position[0],position[1]]=3
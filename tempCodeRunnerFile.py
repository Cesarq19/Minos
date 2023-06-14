from flood_fill_algo import flood_fill

algoritmo=flood_fill()
algoritmo.flood_fill_llenado(3,2)
algoritmo.maze_hwalls[1][1]=3
algoritmo.maze_vwalls[1][1]=2
algoritmo.flood_fill_llenado(3,2)
print(algoritmo.maze_hwalls)
print(algoritmo.maze_vwalls)
print(algoritmo.maze_weights)
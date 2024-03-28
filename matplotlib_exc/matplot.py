import matplotlib.pyplot as plt
#trae el submódulo pyplot de matplotlib que es donde está la mayoría de las cosas y le pone un apodo
import numpy as np
#es una librería que da soporte para crear vectores, matrices y matemáticas de alto nivel


#una línea desde la posición (0,0) hasta la posición (8,10)
xpoints = np.array([1,4,8]) #un arreglo que contiene las x
ypoints = np.array([3,10,2]) #lo mismo de arriba pero con las y

'''
Con lo de arriba solamente creamos una línea uniendo dos puntos, pero podemos hacer más líneas
mediante la creación de varios puntos, por ejemplo:
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
'''

'''
Otra notación para esto, es que podemos crear solamente un arreglo con las y (ypoints), al hacer esto
las x tomarán automáticametne valores de 1, 2, 3, 4...
'''


'''
el plot dibuja puntos en un diagrama, de forma predeterminada, pero esto se puede quitar con
plt.plot(xpoints, ypoints, 'o') agregando la o.

Otra cosa que podemos añadir es el argumento "marker". Este bichito nos cambia la imagen o la
presentación de los puntos de la gráfica, por ejemplo:
plt.plot(xpoints, ypoints, marker = '*') también sirve con 'o', ',', 'x' y muchos más.

También hay un argumento "fmt" que consta del marker|line|color, por lo que mediante este es posible
modificar el la línea que une los puntos. Para las líneas se puede con : -- ._ - _.
Para los colores está r (red), g (green), b (blue), c (cyan), m (magenta), y (yellow), k (black), w (white).

Se puede modificar el tamaño del marcador con el argumento "markersize (ms)". Adicional a esto, se le
pueden modificar el color del borde de los marcadores con "markeredgecolor (mec)". Además, es posible
cambiar el color dentro de los bordes de los marcadores con "markerfacecolor (mfc)"

Cabe aclarar que los colores presentados son atajos, ya que también recibe colores hexadecimales y algunas
palabras como 'hotpink'.
'''
plt.plot(xpoints, ypoints, "*:b", ms = 20, mec = 'k', mfc = 'w')
plt.show()

#creación (plot) y dibujo (show)
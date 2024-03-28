#hice otro porque poner todos los ejercicios en un solo archivo no aguanta

import matplotlib.pyplot as plt
import numpy as np

#en el anterior coso vimos más que todo los marcadores, ahora veremos algo sobre las líneas

ypoints = np.array([3, 8, 1, 10])

#con linestyle (ls) se le puede cambiar el estilo de línea, con dotted queda punteada, por lo que
#se puede inferir que se pueden usar otras palabras para otros estilos
#hay hasta atajos, es decir, en vez de usar linestyle, usar ls y en vez de escribir la palabra
#se pueden usar - : -- y los que habíamos visto

'''
El color de la línea se puede cambiar con el argumento "color (c)". También recibe hexadecimal y
ciertas palabras igual que con los marcadores.

El ancho dela línea también es modificable. Esto s hace mediante "linewidth (lw)" y el valor es un
número decimal (con punto).
'''
plt.plot(ypoints, ls = ':', c = 'r', lw = '18.3')
plt.show()
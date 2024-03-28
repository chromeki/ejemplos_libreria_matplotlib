import matplotlib.pyplot as plt
import numpy as np

#es posible crear barras mediante el uso de estas librerías
#en 'x' podríamos los nombres de las barras y en 'y' los
#valores de estas

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = 'red', width = '0.1')
'''
si se desea visualizar las barras de forma horizontal, en
vez de escribir bar(), se escribe barh()

el argumento color cambia el color de las barras, este
argumento recibe palabras clave y colores hexadecimales

width modifica el ancho de las barras, en caso de que las
barras sean horizontales, no se usa width, se usa height
'''
plt.show()
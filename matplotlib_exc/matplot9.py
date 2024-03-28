import numpy as np
import matplotlib.pyplot as plt

#para la creación de gráficos circulares se usa la función pie()

y = np.array([35, 25, 25, 15]) #asumo que la suma de los valores debe dar 100(%)

#el primer valor que se le brinda lo dibuja sobre el eje x y en el sentido
#antihorario

'''
El tamaño de cada cuña se determina comparando el valor con todos los demás valores,
utilizando esta fórmula:

El valor dividido por la suma de todos los valores: x/sum(x)
'''

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#mediante esto le ponemos nombres a cada una de las piezas/cuñas(?)

myexplode = [0.2, 0, 0, 0]

mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode, shadow = True, 
        colors = mycolors)
'''
como se mencionó, en la creación de las piezas se usa de forma predeterminada
el eje x (0 grados), pero se puede modificar con startangle, en el ejemplo
inciaría con 90 grados, podría verse como el eje y

además está explode, que destaca las piezas que indiquemos, por defecto es 'none',
es decir, no destaca ninguna, pero si se especifica con una lista podemos añadir
esta visual

con shadow es posible añadir sombras dándole el valor 'True' (por defecto es 'False')

los colores son modificables de una forma similar a explode. Se indican los colores en
orden de creación de las piezas y listo (recibe palabras clave y hexadecimales)
'''

plt.legend(title = "Four Fruits:")
#con esto se añade un texto guía por decirlo de alguna forma, se entenderá mejor al
#observarlo. Además se le puede añadir un título si le damos el argumento title

plt.show()
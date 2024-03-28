import matplotlib.pyplot as plt
import numpy as np

#en lo que se ha visto, al crear tramas, todas se ven en la misma gráfica, así que ahora
#se aprenderá a crear "múltiples" gráficas.

'''
Mediante la función subplot() es posible crear lo que se mencionó con anterioridad.

Todo se fue comentando ahí mismo la verdad.

Para poner los títulos en cada una de las gráficas debe hacerse en orden, para no perderse
lo mejor sería debajo del plot de cada una de las gráficas. En este ejercicio queda feo
porque los números se intersectan con las letras, pero se puede cambiar poniendo a todos en
fila y ya. Como cada bicho tiene su título, también es posible que todos tengan un título
general, uno global, uno compartido, eso mediante suptitle().
'''

#plot 1:
x = np.array([1, 2, 3])
y = np.array([8, 5, 12])

plt.subplot(2, 2, 1) #cantidad de filas, columnas y el índice o posición
plt.plot(x,y)
plt.title("Gráfica 1")

#plot 2:
x = np.array([0, 1, 2, 4])
y = np.array([10, 9, 15, 32])

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("Gráfica 2")

#aparentemente los 2 primeros parámetros deben ser iguales en ambos casos

#lo de acá en adelante es fumao experimento
#salió BIEN

font1 = {'family':'serif', 'color':'r', 'size':100}

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("Gráfica 3")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("Gráfica 4")

#los dos primeros parámetros de subplot() deben ir iguales ya que crean una tabla, con cierta
#cantidad de filas y columnas, lo otro ya es la posición que ocupan dentro de dicha tabla

plt.suptitle("aloha", fontdict = font1)

plt.show()

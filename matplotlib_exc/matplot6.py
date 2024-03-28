import matplotlib.pyplot as plt
import numpy as np

#algo útil para implementar es el mapa de colores, que es una barra
'''
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors, cmap='viridis', s = 'sizes', alpha=0.5)
#cmap para implementar coso en vez de vidris hay más valores que se le pueden dar a este argumento
#s para variar el tamaño de cada marcador y alpha para cambiar la transparencia


plt.colorbar() #para mostrar la barra

plt.show()
'''

#este es un mejor ejempllo y se ve más colorido la verdad, pura estética mano
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
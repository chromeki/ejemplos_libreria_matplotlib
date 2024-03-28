import matplotlib.pyplot as plt
import numpy as np

#un histograma es un gráfico que muestra distribuciones de frecuencia
#es un gráfico que muestra el número de observaciones dentro de cada intervalo dado

#para la creación de un histograma se usa la función hist(), que utilizará una matriz
#de números para su creación, la matriz se envía a la función como argumento

#para no tener que inventar datos en este ejercicio, pueden ser generados
#automática y aleatoriamente mediante numpy

x = np.random.normal(170, 10, 250)

#se crea una matriz aleatoria con 250 valores, dichos valores se concentrarán alrededor
#de 170 y la desviación estándar es de 10
#con print(X) es posible ver los valores generados

plt.hist(x)

plt.show()

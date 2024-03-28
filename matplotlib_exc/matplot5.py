import matplotlib.pyplot as plt
import numpy as np

#ya se vio que en las gráficas los puntos que se crean son unidos automáticamente
#pero podemos evitar que esto pase creando un diagrama de dispersión con la función
#scatter()

#se le puede cambiar el color a los marcadores con "color (C)"
'''
También se le puede cambiar el color a cada uno de los marcadores con este ejemplo:

    colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

    plt.scatter(x, y, c=colors)

'''

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x , y, c = '#88c999')

#es posible crear varios, por ejemplo, para ver qué tan rápido va un coche según su
#antigüedad en el primer día y crear otro diagrama de dispersión para el día dos
#de la siguiente forma

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x , y, c = '#000000')

plt.show()
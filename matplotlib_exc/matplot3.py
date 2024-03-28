import matplotlib.pyplot as plt
import numpy as np

'''
Otra opción que nos ofrece esta librería es la de agregar varias "gráficas" y no solamente
limitarnos a una. Para realizar esto hay varias formas:

- Forma 1:
    Creando dos líneas y usar la función de dibujo dos veces:

        y1 = np.array([3, 8, 1, 10])
        y2 = np.array([6, 2, 7, 11])

        plt.plot(y1)
        plt.plot(y2)

        plt.show()

- Forma 2:
    Crear tanto los x como los y para cada una de las gráficas y agregarlas en orden dentro
    del plot():

        x1 = np.array([0, 1, 2, 3])
        y1 = np.array([3, 8, 1, 10])
        x2 = np.array([0 , 2, 4, 6])
        y2 = np.array([6, 2, 7, 11])

        plt.plot(x1, y1, x2, y2)

        plt.show()
'''


'''
Otra ayuda es que le podemos poner etiquetas/título/texto al eje x, el eje y, título de la gráfica/trama.
Además de agregar esto, podemos modificar la fuente de letra y el posicionamiento de este.

Vamos en orden. Para agregar el título, las etiquetas para x e y se harán así respectivamente:
    plt.title("Título")
    plt.xlabel("Etiqueta x")
    plt.ylabel("Etiqueta y")

Para cambiar las propiedades de este texto se hará mediante la creación de diccionarios y mediante el
parámetro fontdict. Por ejemplo:
    font1 = {'family':'serif', 'color':'blue', 'size':20}
    font2 = {'family':'serif', 'color':'darked', 'size':15}

    plt.title("Título", fontdict = font1)
    plt.xlabel("Etiqueta x", fontdict = font2)
    plt.ylabel("Etiqueta y", fontdict = font2)

Por último, para posicionar el título se logra mediante el parámetro "loc" dentro de title(). Los valores
que podemos insertar son de derecha, centro e izquierda. Se logra de la siguiente forma:
    plt.title("Título", loc = 'left')
'''

#es posible establecer cuadrículas para la gráfica mediante la función grid(), que tiene una
#variedad de parámetros y propiedades

'''
Usando solamente grid() se agrega una cuadrícula automáticamente, es decir, muestra líneas en el eje x
y en el eje y. Podemos especificar si mostrar líneas solamente en un eje mediante el parámetro 'asis'.
grid(axis = 'x') para mostrar solamente las líneas PARA el eje x como cuadrícula o grid(xsis = 'y').

Lo chévere es que podemos modificarlas mediante las propiedades de línea:
    grid(color = ' color ', estilo de línea = ' estilo de línea ', ancho de línea = número)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

'''

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0 , 2, 4, 6])
y2 = np.array([6, 2, 7, 11])

font1 = {'family':'serif', 'color':'#000', 'size':20}
font2 = {'family':'serif', 'color':'#000', 'size':15}

plt.title("Título", fontdict = font1, loc = 'right')
plt.xlabel("Etiqueta x", fontdict = font2)
plt.ylabel("Etiqueta y", fontdict = font2)

plt.plot(x1, y1)
plt.plot(x2, y2, ls = ':')

plt.grid(axis = 'x', color = 'r', linewidth = '0.7', linestyle = ':')

plt.show()
import numpy as np

lista1 = np.array([int(input(f"Ingrese el elemento {i+1} de la primera lista: ")) for i in range(5)])
lista2 = np.array([int(input(f"Ingrese el elemento {i+1} de la segunda lista: ")) for i in range(5)])


print(lista1 * lista2)


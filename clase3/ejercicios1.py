numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numeros.sort()

print("Los números ordenados son:", numeros)
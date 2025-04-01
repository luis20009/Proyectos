# Definir las dos listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

# Verificar si lista2 es igual a lista1 invertida
if lista1 == lista2[::-1]:
    print("Las listas son iguales en direcciones opuestas.")
else:
    print("Las listas no son iguales en direcciones opuestas.")

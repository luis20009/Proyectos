x = int(input("Ingrese su número: "))
lista = []
resultados = []

total = count = 0

# Validar que el número sea mayor que 1
while x < 2:
    print("Debes ingresar un número entero mayor a uno")
    x = int(input("Ingrese su número: "))

# Generar la lista inicial
while count <= x:
    total += count
    lista.append(count)
    count += 1

# Operar sobre la lista para generar los resultados acumulativos
for i in range(len(lista) - 1):  # Asegurar que no se desborde el índice
    suma = lista[i] + lista[i + 1]
    resultados.append(suma)

    # Actualizar elementos de la lista para el siguiente cálculo
    lista[i] = lista[i + 1]
    lista[i + 1] = suma

    if suma < x + 1:
        print(f"Mira: {resultados}") 
        print(suma)

# Introducir variación usando el tiempo interno del programa
# Por ejemplo, usar el resto de dividir el total acumulado entre la longitud
indice_aleatorio = (total + len(lista) * (total % 7)) % len(lista)

# Eliminar el número en el índice generado
numero_eliminado = lista.pop(indice_aleatorio)

# Mostrar el resultado final
print(f"Se eliminó el número: {numero_eliminado}")
print("Lista final modificada:", lista)
print("Total acumulado:", total)

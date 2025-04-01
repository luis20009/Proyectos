# Definir las variables
variable1 = 10
variable2 = 20
variable3 = 30
variable4 = 40

# Mostrar las variables disponibles
print("Variables disponibles:")
print("1. Variable 1 (10)")
print("2. Variable 2 (20)")
print("3. Variable 3 (30)")
print("4. Variable 4 (40)")

# Solicitar al usuario que elija las variables a sumar
eleccion1 = int(input("Elige la primera variable a sumar (1-4): "))
eleccion2 = int(input("Elige la segunda variable a sumar (1-4): "))

# Obtener los valores de las variables elegidas
variables = [variable1, variable2, variable3, variable4]
suma = variables[eleccion1 - 1] + variables[eleccion2 - 1]

# Mostrar el resultado
print(f"La suma de la variable {eleccion1} y la variable {eleccion2} es {suma}")
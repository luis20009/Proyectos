# Inicializar el inventario como un diccionario
inventario = {}

# Pedir al usuario que ingrese el número de tipos de productos
num_productos = int(input("Ingrese el número de tipos de productos: "))

# Recopilar información sobre cada producto
for _ in range(num_productos):
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
    precio = float(input(f"Ingrese el precio de {nombre_producto}: "))
    inventario[nombre_producto] = {'cantidad': cantidad, 'precio': precio}

# Calcular el valor total del inventario
valor_total = sum(item['cantidad'] * item['precio'] for item in inventario.values())

# Mostrar el inventario y el valor total
print("\nInventario:")
for producto, info in inventario.items():
    print(f"{producto}: {info['cantidad']} unidades a ${info['precio']} cada una")

print(f"\nValor total si vendiera todo: ${valor_total:.2f}")

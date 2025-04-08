print("Bienvenido, querido trabajador")
x = int(input("Número de productos: "))

def menu():
    print("Deposite los siguientes datos")
    nombre = input("Nombre del producto: ")
    valor = int(input("Ingresar valor del producto: "))
    cantidad = int(input("Cantidad: "))
    total = valor * cantidad
    return nombre, valor, cantidad, total

productos = []

for _ in range(x):
    producto = menu()
    productos.append(producto)

print("\nProductos ingresados:")
for producto in productos:
    print(f"Nombre: {producto[0]}, Valor: {producto[1]}, Cantidad: {producto[2]}, Total: {producto[3]}")

    
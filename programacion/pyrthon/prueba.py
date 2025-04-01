print("Bienvenido querido trabajador")
x = int(input("Ingrese cantidad de productos"))
total_venta = 0
nombre_productos= []
def Menu_options():
      global total_venta
      print("Porfavor ingresar los siguientes datos")
      Name = input("Nombre del producto: ")
      nombre_productos.append(Name)
      Cantidad = int(input(f"cantidad de {Name}:"))
      precio = int(input(f"Precio de {Name}:"))
      total = Cantidad * precio
      total_venta += total
      print(total, f"Total de la venta de {Name}")
      
      print("Nombres de los productos ingresados")
     
for _ in range(x):
 Menu_options()


for name in nombre_productos:
          print(name)

print(total_venta, f"Total de la suma de los productos vendidos")

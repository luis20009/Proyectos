x=(input("Ingrese el numero a comprobar: "))
numeros=[]
mi_lista_numerica = [int(y) for y in x]
for i in mi_lista_numerica:
   numeros.append(i**len(x))
if sum(numeros) == int(x):
   print("Es un numero de Amstrong")
else:
   print("No es un numero de Amstrong")
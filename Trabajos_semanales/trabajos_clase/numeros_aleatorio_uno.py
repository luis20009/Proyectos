x=int(input("Ingrese su numero: "))
lista=[]
resultados=[]
total=count=0
suma_total=0
while x<2:
    print("Debes ingresar un numero entero mayor a uno")
    x=int(input("Ingrese su numero: "))
while count<=x:
    total+=count
    lista.append(count)
    count+=1
for i in range(len(lista)-1):
         suma=(lista[i]+lista[i+1])
         resultados.append(suma)
         lista[i] = lista[i + 1]
         lista[i + 1] = suma
         if suma>=lista[-1]:
              break
print("Listado de los numeros: ",lista)
print("Mira un valor que es mas o menos cercano: ",suma)
sos=((sum(resultados)*7)%(sum(lista)//sum(resultados))**(sum(lista)))
perico=list(str(int(sos)))
medio_pe=len(perico)//2
doto_medio=lista[medio_pe]
lista.remove(doto_medio)
print("Numero borrado: ",doto_medio)
print("Listado nueva de los numeros: ",lista)

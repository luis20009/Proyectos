dato = ['Nombre','Contraseña','Correo','Edad']
lista1={}
nombes=[]
nombes2=[]
def opcion_1():
    x=int(input("Ingrese la cxantidad de usuarios"))
    absolute=[]
    for i in range(x):
        lista1={}
        for d in dato:
                 
                  valor=input(f"Ingrese su {d}")
                  lista1[d]=valor
        absolute.append(lista1)
    print(absolute)

    for name in absolute:  
        nombes.append(name['Nombre']) 
        nombes2.append(name['Nombre'])

    if nombes == nombes2:
          print("pene")
        


opcion_1()










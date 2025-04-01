from num2words import num2words
import time as wait
import os
lista={'Nombre':'Juan','Contraseña':123456,'Edad':15,'Correo':'juan@gmail.com'}
datos=['Nombre','Contraseña','Edad','Correo']
batman=[lista]
i=0

def new_user():
    os.system('cls') 
    cantidad=int(input("Ingrese la cantidad deseada: "))
    for i in range(cantidad):
        i += 1
        numero_en_palabras = num2words(i, lang='es')
        lista1={}
        for dato in datos:
         valores=input(f"Ingrese su {dato}_{numero_en_palabras}: ")
         if dato == 'Correo':
             while "@" not in valores or "." not in valores.split("@")[-1]:
                   print("Correo electrónico inválido. Debe contener un '@' y un dominio válido.")
                   valores = input("Ingrese su correo: ")
         elif dato == 'Contraseña':
                while len(valores)<=5:
                     print("Su contraseña debe tener por lo menos 6 numeros")
                     valores=input(f"ingrese su {dato}: ")
         elif dato == 'Nombre':
                while any(usuario['Nombre'] == valores for usuario in batman):
                    print("Nombre reptido en el sistema")
                    valores=input("Ingrese su nombre: ")
        
         elif dato == 'Edad':
                 while not valores.isdigit() or int(valores) <= 0:
                     print("Edad inválida. Debe ser un número mayor que 0: ")
                     valores = input("Ingrese su edad: ")
                 valores = int(valores)
         lista1[dato] = valores
        print(f"Tu creaste la siguiente informacion: {lista1}")
        batman.append(lista1)
        wait.sleep(2)
        input("Presiona ENTER para seguir")
        os.system('cls') 
        

def all_user():
    os.system('cls') 
    for user in batman:
     print(f"A continuacion vera todos los usuarion que estan en el sistema\n{user}")
    wait.sleep(2)
    input("Presiona ENTER para seguir")
   
def salir():
    print("Good bye") 
    exit()
    os.system('cls')
    
def menu():
    os.system('cls') 
    print("\nMenu:\n1.Introducir un  nuevo usuario\n2.Mostar todos los usuarios existentes\n3.Salir")
   
opciones={1:new_user, 2: all_user, 3:salir}

while True:
 try:
       menu()
       op= int(input("Ingrese su opcion deseada: "))
       while op not in [1,2,3]:
               print("opcion invalida")
               op= int(input("Ingrese su opcion deseada: "))
       verificador = opciones.get(op)   
       verificador()
     
 except ValueError:
        print('Dato incorrecto')



    
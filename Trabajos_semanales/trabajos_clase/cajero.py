x = "1234"
y = "1234"
saldo = 100

print("Bienvenido querido usuario")
cuenta = input("Ingrese su número de cuenta: ")
while cuenta != x:
    print("El valor de la cuenta es incorrecto")
    cuenta = input("Ingresar valor de la cuenta: ")
print("Cuenta correcta") 

pin = input("Ingrese su PIN de cuenta: ")
while pin != y:
    print("El PIN de la cuenta es incorrecto")
    pin = input("Ingresar PIN de la cuenta: ")
print("Contraseña correcta")  

def mostrar_menu():
    print("\nMenú:")
    print("1. Retirar")
    print("2. Depositar")
    print("3. Cambiar contraseña")
    print("4. Salir")

while True:
    mostrar_menu()
    op = input("Por favor, escoja una opción: ")

    if op == "1":
        monto = float(input("Por favor ingrese el monto a retirar: "))
        if monto > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= monto
            print("Tu nuevo saldo es:", saldo)
        input("¿Desea salir? (presione Enter para continuar)")
        print("1. Sí")
        print("2. No")
        xi = input("Ingrese la opción: ")
        if xi == "1":
            print("Hasta luego")
            break
        elif xi == "2":
            continue

    elif op == "2":
        monto = float(input("Por favor ingrese el monto a depositar: "))
        saldo += monto
        print("Tu nuevo saldo es:", saldo)
        input("¿Desea salir? (presione Enter para continuar)")
        print("1. Sí")
        print("2. No")
        xi = input("Ingrese la opción: ")
        if xi == "1":
            print("Hasta luego")
            break
        elif xi == "2":
            continue

    elif op == "3":
        nueva_contraseña = input("Ingrese su nueva contraseña: ")
        x = nueva_contraseña
        print("Tu nueva contraseña es:", x)
        input("¿Desea salir? (presione Enter para continuar)")
        print("1. Sí")
        print("2. No")
        xi = input("Ingrese la opción: ")
        if xi == "1":
            print("Hasta luego")
            break
        elif xi == "2":
            continue

    elif op == "4":
        print("Hasta luego")
        break

    else:
        print("Opción no válida, intenta de nuevo.")


 




  

 
  


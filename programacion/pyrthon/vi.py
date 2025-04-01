edad = int(input("Ingrese edad"))
Mont = int(input("Ingrese valor del monto"))
pais= input("Ingrese pais").strip().lower()
paises=["mexico","colombia"]
if edad>18:
    if pais =="españa":
        op=Mont*0.90
        print("Tienes un descuento del 9%")
        print(op)
    elif pais in paises:
       op = Mont*0.85
       print("Tienes un descuento del 8.5%")
       print(op)
    else:
        print("Este es tu valor")
        print(Mont)
else:
    print(f"No cumples los requerimientos, {edad}")

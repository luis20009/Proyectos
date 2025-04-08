def operaciones():
    try:
        op=int(input("Escoja su figura:\n1.Triangulo\n2.Cuadrado\n3.Rectangulo\n\nIngrese la opcion: "))
        while op not in [1,2,3]:
         return 'valor invalido'
    
        if op==1:
         B=int(input("Ingrese su base: "))
         H=int(input("Ingrese su altura: "))
         Result=(B*H)/2
         return (f"su resultado es: {Result}")
        if op==2:
         B=int(input("Ingrese su base o un lado: "))
         Result=(B**2)
         return (f"su resultado es: {Result}")
        if op==3:
         B=int(input("Ingrese su base: "))
         H=int(input("Ingrese su altura: "))
         Result=(B*H)
         return (f"su resultado es: {Result}")
    except ValueError:
       return 'valor invalido'
print(operaciones())
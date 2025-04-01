cuenta = float(input("Ingrese el valor pagado"))
print("Tu cuenta en base es", cuenta)
if 100 <=cuenta<500:
    Result = cuenta * 0.01
    print("obtuviste un descuento 10%")
    print(Result)
elif cuenta>=500:
    Result = cuenta * 0.05
    print("obtuviste un descuento 50%")
    print(Result)
else:
    ("No obtuvo ningun descuento")

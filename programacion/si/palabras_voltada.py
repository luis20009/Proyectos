alrevez=[]
frase=input("Ingrese la palabra ")

print('Esta es su frase: ',list(frase))
m=len(frase)
for i in range(m):
         alrevez.append(frase[m - i -1 ])
if alrevez == list(frase):
        print("Es un palindromo")
else:
        print("No es igual")
print('Frase mezclado: ',alrevez)
print(frase[::-1])
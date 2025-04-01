alrevez=[]
frases=[]
frase=(input("Ingrese su palabra"))

frases.append(list(frase))
print('Su palabra inicial',frases[0])
m=len(frase)
for i in range(m):
        alrevez.append(frase[m - i -1 ])
print("Primer carácter:", frase[0])
print("Lista invertida:", alrevez)
print("Lista original como lista de caracteres:", list(frase))
print("Frases original:", frases)



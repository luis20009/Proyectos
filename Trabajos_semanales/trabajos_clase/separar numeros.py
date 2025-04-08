lista=[5,64,986,3,4,60,457,105,688,42] 
entero=[]
n_entero=[]
for num in lista:
    residuo=num%2
    if residuo==0:
        entero.append(num)
    else:
        n_entero.append(num)
print(f"Estos son los enteros: {entero}")
print(f"Estos son los impares: {n_entero}")
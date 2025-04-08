lista=[]
primo=[]
no_primo=[]
count=0
for count in range(1,101):
    lista.append(count)
    divisores=0
    for divisor in range(1,count+1):
        if (count%divisor)==0:
            divisores+=1
    if divisores==2:
        primo.append(count)
    else: 
        no_primo.append(count)
   
print(f"Es primo: {primo}\nNo es primo: {no_primo}")

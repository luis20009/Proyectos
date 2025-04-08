import os as borrador
potenciador=[]
class personaje:
    def __init__(self,nombre,vida,daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
    
    def dañar(self,enemigo,familiar):
        if familiar.vida <= 0:
            familiar.daño = 0
            print(f"{familiar.nombre}, murio")
        self.daño += familiar.daño
        enemigo.vida -= self.daño
        print(f"{self.nombre} causo {self.daño} de daño a {enemigo.nombre}, tambien {familiar.nombre} causo {familiar.daño} de daño")
        print(f"la nueva vida de {enemigo.nombre} es {enemigo.vida}")
    def status(self,enemigo,familiar):
        if familiar.vida <= 0:
            familiar.daño = 0
            familiar.vida=0
            print(f"{familiar.nombre}, murio")
        print(f"La vida de {self.nombre} es: {self.vida}\nLa vida de {enemigo.nombre} es: {enemigo.vida}\nLa vida de {familiar.nombre} es {familiar.vida}")
    def plus(self):
        print("Usate habilidad de envenenamiento, ahora tienes una bonificacion de atacaque de +15 puntos de daño")
        self.daño+=15
class enemigo:
    def __init__(self,nombre,vida,daño):
         self.nombre = nombre
         self.vida = vida
         self.daño = daño
    def dañar(self,personaje,familiar):   
        personaje.vida -= self.daño
        familiar.vida -= self.daño
        if familiar.vida <= 0:
            familiar.daño = 0
            familiar.vida=0
        print(f"{self.nombre} causo {self.daño} de daño a {personaje.nombre} y a {familiar.nombre}, ahora la vida de{familiar.nombre} es {familiar.vida}")
        print(f"la nueva vida de {personaje.nombre} es {personaje.vida}")
class familiar:
    def __init__(self,daño,vida,nombre):
        self.daño=daño
        self.vida=vida
        self.nombre=nombre


family=[familiar(5,12,"gato"),familiar(9,13,"lobo"),familiar(190,1,"cuy")]
heroes= [personaje("raul",100,15),
         personaje("Merlin",110,8),
         personaje("barbaro",70,36)
         ]
print("Escoge tu personaje:")
for i, juagador in enumerate(heroes):
 print(f"{i + 1}. {juagador.nombre} (Vida: {juagador.vida}, Daño: {juagador.daño})")
eleccion = int(input("\nEscribe el número de tu personaje elegido: "))
heroe = heroes[eleccion - 1]
print("Escoge tu mascota:")
for ñ, familiax in enumerate(family):
 print(f"{ñ + 1}. {familiax.nombre} (Vida: {familiax.vida}, Daño: {familiax.daño})")
eleccion = int(input("\nEscribe el número de tu mascota elegida: "))
mascota = family[eleccion - 1]
villano=enemigo("veneco",100,25)
while heroe.vida>0 and villano.vida>0:
    o=0
    x=int(input("\nQue quieres hacer\n1.Atacar\n2.Ver tu estado\n3.Habilidad especial\nIngrese su opcion: "))
    borrador.system('cls')
    while x not in [1,2,3]:
        print("opcion no valida")
        x=input("Que quieres hacer\n1.Atacar\n2.Ver tu estado\nIngrese su opcion: ")
        borrador.system('cls') 
    if x==1:
        heroe.dañar(villano,mascota)
        input("\nPresione enter para continuar: ")     
    elif x==2:
        heroe.status(villano,mascota)
        input("\nPresione enter para continuar: ")
        borrador.system('cls')
    else:
        if len((potenciador))>=1:
            print("Ya usate la habilidad, tienes que esperar un turno")
            potenciador.clear()
            x=int(input("\nQue quieres hacer\n1.Atacar\n2.Ver tu estado\n3.Habilidad especial\nIngrese su opcion: "))
            borrador.system('cls')
        heroe.plus()
        potenciador.append(1)
        input("\nPresione enter para continuar: ")
        borrador.system('cls')
    input("\nPresione enter para continuar: ")
    borrador.system('cls')
if heroe.vida > 0:
    print(f"¡{heroe.nombre} ganó!")
else:
    print(f"¡{villano.nombre} ganó!")

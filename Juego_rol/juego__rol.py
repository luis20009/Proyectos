potenciador=[]
import random
import os
def borrar():
    columns, _ = os.get_terminal_size()
    texto = "///Presione ENTER para continuar///"
    espacios = (columns - len(texto)) // 2
    input(" " * espacios + texto)
    os.system('cls')
class personaje:
    def __init__(self,nombre,vida,daño,plus):
        self.nombre=nombre
        self.vida=vida
        self.vida_inicial_ = vida
        self.daño=daño
        self.plus=plus
    def dañar(self,malo,animal):
        if animal.vida<0:
            malo.vida-=self.daño
            print(f"{self.nombre} causo {self.daño} a {malo.nombre}\nLa nueva vida de {malo.nombre} es {malo.vida}")
        else:
         self.daño+=animal.daño
         malo.vida-=self.daño
         print(f"{self.nombre} y {animal.nombre} causaron {self.daño} de daño a {malo.nombre}\nLa nueva vida de {malo.nombre} es {malo.vida}")
    def status(self,malo,animal):
        if animal.vida>0:
         print(f"Tu vida es {self.vida}\nLa vida de tu mascota es {animal.vida}\nLa de tu rival es {malo.vida}")
        else:
           print(f"Tu vida es {self.vida}\nTu mascota esta muerta\nLa de tu rival es {malo.vida}")
           
    def plusx(self,malo):
        if self.plus=="veneno":
            malo.vida-=30
            print(f"{self.nombre} causo {30} de daño a {malo.nombre} debido a su habilidad veneno\nLa nueva vida de {malo.nombre} es {malo.vida}")
        elif self.plus=="regenerar":
            self.vida+=26
            print(f"{self.nombre} uso su habilidad de regeneracion y recupero {26} de vida\nTu nueva vida es {self.vida}")
        else:
            fuerza_extra=10
            self.daño+=fuerza_extra
            print(f"Usaste tu habilidad de aumentar la fuerza, pasando esta a ser {self.daño} ")
    def restaurar(self):
       self.vida=self.vida_inicial_
       print(f"{self.nombre} ha restaurado su vida a {self.vida}")

class animal:
    def __init__(self,nombre,vida,daño,clase,color):
        self.nombre=nombre
        self.vida=vida
        self.daño=daño
        self.clase=clase
        self.color=color
class malo:
    def __init__(self,nombre,vida,daño,plus):
        self.nombre=nombre
        self.vida=vida
        self.daño=daño
        self.plus=plus
    
    def accion_al_azar(self,personaje,animal):
        acciones = [1,2]
        accion_elegida = random.choice(acciones)
        if accion_elegida == 1:
            personaje.vida-=self.daño
            animal.vida-=self.daño
            if animal.vida<0:
             personaje.vida-=self.daño
             print(f"\n{self.nombre} causo {self.daño} de daño a {personaje.nombre}\nLa nueva vida de {personaje.nombre} es {personaje.vida}")
            else:
             print(f"\n{self.nombre} causo {self.daño} de daño a {personaje.nombre} y a {animal.nombre}\nLa nueva vida de {personaje.nombre} es {personaje.vida} y la de {animal.nombre} es {animal.vida} ")
        else:
            if self.plus=="veneno":
              personaje.vida-=30
              animal.vida-=5
              if animal.vida>0:
               print(f"\n{self.nombre} causo {30} de daño a {personaje.nombre} debido a su habilidad veneno\nTu vida es {personaje.vida}\nLa vida de {animal.nombre} es {animal.vida}")
              else:
                  print(f"\n{self.nombre} causo {30} de daño a {personaje.nombre} debido a su habilidad veneno")
                 
            elif self.plus=="regenerar":
             self.vida+=26
             print(f"\n{self.nombre} uso su habilidad de regeneracion y recupero {26} de vida")
            elif self.plus=="fuerza extra":
             fuerza_extra=10
             self.daño+=fuerza_extra
             print(f"\nUsaste tu habilidad de aumentar la fuerza, pasando esta a ser {self.daño} ")
       
heroes= [personaje("enano",100,10,"veneno"),
         personaje("mago",110,9,"regenerar"),
         personaje("barbaro",70,12,"fuerza extra")
         ]
family=[animal("Geku",20,4,"gato","blanco"),animal("Mitsuku",19,6,"cuy","negro"),animal("Botif",18,6,"Lobo","negro")]
for i, jugador in enumerate(heroes):
    print(f"{i + 1}. {jugador.nombre} (Vida: {jugador.vida}, Daño: {jugador.daño}, Habilidad: {jugador.plus})")


eleccion = int(input("\nEscribe el número de tu personaje elegido: "))
while eleccion not in [1,2,3]:
     eleccion=int(input("Opcion invalida\nIngrese otra opcion: "))
borrar()
heroe = heroes[eleccion - 1]
heroe.nombre=input("Elegí un nombre para tu personaje: ")
borrar()
print("Ahora escoje a un acompañante: ")

for u, familiar in enumerate(family):
 print(f"{u + 1}. {familiar.nombre} (Clase: {familiar.clase}, Vida: {familiar.vida}, Daño: {familiar.daño})")
eleccione =int(input("\nEscribe el numero de tu mascota elegida: "))
while eleccion not in [1,2,3]:
     eleccione=int(input("Opcion invalida\nIngrese otra opcion: "))
acompañante = family[eleccione - 1]
borrar()
print(f"Bienvenido {heroe.nombre}")
borrar()

print(f"""
        En el reino de Eldoria, una tierra de vastos bosques encantados y montañas que susurraban secretos, vivía {heroe.nombre}, el Guerrero de la Llama. 
       Su destino estaba marcado desde el momento en que sostuvo la espada ignífuga llamada "Furia Ardiente," una reliquia capaz de incinerar la oscuridad. 
       {heroe.nombre} no era solo un guerrero; era la última esperanza de su pueblo, que vivía bajo el yugo de tres temibles villanos.
       """)
borrar()
print(f"""
        {heroe.nombre} emprendió su travesía, acompañado por su fiel mascota, un {acompañante.clase} {acompañante.color} llamado {acompañante.nombre}, que llevaba las marcas de los antiguos espíritus en su pelaje.
        Su misión era clara: liberar Eldoria de la oscuridad al derrotar a los tres villanos.
       """)
borrar()
villano=malo("Yomungaderk",90,13,"veneno")
def peleas():
 print(f"El enemigo a enfrentar sera {villano.nombre}\nAhora preparate para la lucha")
 borrar()

 while True:
   try:
      while heroe.vida>0 and villano.vida>0:
        x=int(input("\nQue quieres hacer\n1.Atacar\n2.Ver tu estado\n3.Habilidad especial\nIngrese su opcion: "))
        borrar()
        while x not in [1,2,3]:
          print("opcion no valida")
          x=int(input("Que quieres hacer\n1.Atacar\n2.Ver tu estado\n3.Habilidad especial\nIngrese su opcion: "))
          borrar()
        if x==1:
           if len((potenciador))>=1:
                potenciador.clear()
           heroe.dañar(villano,acompañante)
           villano.accion_al_azar(heroe,acompañante)  
        elif x==2:
          heroe.status(villano,acompañante)
          borrar()
        elif x==3:
         if len((potenciador))>=1:
            print("Ya usate la habilidad, tienes que esperar un turno")
            potenciador.clear()
         else:
          heroe.plusx(villano)
          potenciador.append(1)
          villano.accion_al_azar(heroe,acompañante)  
        borrar()
      if heroe.vida > 0:
       print(f"¡{heroe.nombre} ganó!")
       heroe.restaurar()
       break
      else:
       print(f"¡{villano.nombre} ganó!")
       borrar()
       print("Tu pierdes")
       exit()
       break
   except ValueError:
    print("Elegiste una opcion invalida o pusite un dato mal")
    borrar()
peleas()
borrar()
villano=malo("Artorias",110,13,"regenerar")
peleas()
borrar()
villano=malo("Meroes",120,15,"fuerza extra")
peleas()
borrar()


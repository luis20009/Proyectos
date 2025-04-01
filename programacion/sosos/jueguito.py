# Definir la clase Personaje
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, enemigo):
        if enemigo.vida > 0:
            enemigo.vida -= self.ataque
            print(f"{self.nombre} atacó a {enemigo.nombre}. {enemigo.nombre} tiene ahora {enemigo.vida} puntos de vida.")
        else:
            print(f"{enemigo.nombre} ya fue derrotado.")

    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.vida} puntos de vida y {self.ataque} de ataque.")

# Crear los personajes
jugador = Personaje("Héroe", 100, 20)
enemigo = Personaje("Villano", 50, 15)

# Bucle principal del juego
while enemigo.vida > 0 and jugador.vida > 0:
    print("\n¿Qué quieres hacer?")
    print("1. Atacar al enemigo")
    print("2. Mostrar estado")
    print("3. Salir del juego")
    opcion = input("Elige una opción (1, 2, 3): ")

    if opcion == "1":
        jugador.atacar(enemigo)
        if enemigo.vida > 0:
            enemigo.atacar(jugador)
    elif opcion == "2":
        jugador.mostrar_estado()
        enemigo.mostrar_estado()
    elif opcion == "3":
        print("Has salido del juego.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Verificar quién ganó
if jugador.vida <= 0:
    print("\nEl héroe fue derrotado. ¡Mejor suerte la próxima vez!")
elif enemigo.vida <= 0:
    print("\n¡Has derrotado al enemigo! ¡Felicidades, Héroe!")

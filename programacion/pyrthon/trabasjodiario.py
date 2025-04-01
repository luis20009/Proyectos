import time as pene
name=str(input("Por favor ingrese su nombre: "))
print(f"Hola {name}\nBienvenido a tu gestionador de tareas")
print("Este programa busca:\nayudarte en tu gestion\ndarte algun que otro consejo\nSimplificar tu dia")
Res= input("\n¿Qué te parece si empezamos con tu rutina de hoy? (SI/NO): ").strip().lower()
while Res != "si":
 print("Dime cuando estes listo")
 Res=input("¿Ya estas listo?: ").strip().lower()
print("Entendido")
print("Comnzemos con lo basico")
print("¿Que quieres hacer el dia de hoy?")
def opciones():
 print("\nOPCIONES:")
 print("1.Cardio")
 print("2. Ir al gym")
 print("3. Estudiar")
 print("4. Comer algo sano")
 print("5. nada")
def exercice():
  print("Vamos a romperte con esta rutina")
  print("Primero calentemos: ")
  print("\nCalentamiento (5 minutos): ")
  print("Marcha en el lugar: 2 minutos")
  pene.sleep(1)
  print("Saltos suaves (jumping jacks): 1 minuto")
  pene.sleep(1)
  print("Estiramientos dinámicos (brazos y piernas): 2 minutos")
  pene.sleep(1)
  print("\n Ahora vamos con el entreno: ")
opcionespas_append=[]
polainas = True
while polainas:
 opciones()
 op=int(input("\nIngrese el numero de la opcion: "))
 while op not in [1,2,3,4] or op in opcionespas_append:
   print("Opcion invalida")
   op=int(input("\nIngrese el numero de la opcion: "))
 opcionespas_append.append(op)
 
 if op==1:
  exercice()
  print("Ejercicio Principal (20 minutos)")
  pene.sleep(1)
  print("Correr en el lugar o saltar la cuerda (alternar cada 2 minutos): 10 minutos")
  pene.sleep
  print("Burpees (1 minuto): 3 series de 10 burpees con 1 minuto de descanso entre cada serie")
  pene.sleep(1)
  print("Mountain climbers (1 minuto): 3 series de 20 segundos con 40 segundos de descanso entre cada serie")
  pene.sleep(1)
  print("Rodillas altas (high knees) (1 minuto): 3 series de 20 segundos con 40 segundos de descanso entre cada serie")
  pene.sleep(1)
  print("\nFelicidades terminaste tu cardio")
  print("Ahora escoje otra opcion, recuerda que ya terminaste tu cardio")
 
 if op==2:
  exercice()
  print("Ejercicio Principal (20 minutos)")
  pene.sleep(1)
  print("Sentadillas con barra (Squats): 3 series de 10-12 repeticiones")
  pene.sleep
  print("Remo con barra (Bent-Over Barbell Row):3 series de 10-12 repeticiones")
  pene.sleep(1)
  print("Peso muerto (Deadlift): 3 series de 8-10 repeticiones")
  pene.sleep(1)
  print("Press militar con barra (Overhead Press): 3 series de 8-10 repeticiones")
  pene.sleep(1)
  print("\nFelicidades terminaste tu rutina de full body")
  print("Ahora escoje otra opcion, recuerda que ya terminaste tu rutina de full body")

 if op==3:
  print("Calentamiento Mental (10 minutos):\nEstiramientos rápidos: Estira tus brazos, piernas y cuello\nEjercicio de respiración profunda")
  print("Bloque 1: Lectura Activa (45 minutos)")
  pene.sleep(1)
  print("Bloque 2: Resúmenes y Mapas Mentales (45 minutos)")
  pene.sleep
  print("Descanso (10 minutos)")
  pene.sleep(1)
  print("Práctica y Ejercicios (45 minutos)")
  pene.sleep(1)
  print("Descanso final")
  pene.sleep(1)
  print("\nFelicidades terminaste tu rutina de estudio")
  print("Ahora escoje otra opcion, recuerda que ya terminaste tu rutina de estudio")
 
 if op==4:
  print("Ingredientes: ")
  print("1 taza de quinoa")
  print("2 tazas de agua")
  print("2 pechugas de pollo")
  print("1 aguacate")
  print("1 pimiento rojo")
  print("1 pimiento amarillo")
  print("1/2 taza de frijoles negros")
  print("1/2 taza de maíz")
  print("2 cucharadas de aceite de oliva")
  print("Jugo de 1 limón")
  print("Sal y pimienta al gusto")
  print("Especias al gusto (ajo en polvo, comino, pimentón, etc.)")
  print("Cilantro fresco para decorar")
  print("\n pasasos para preparalo:\nCocinar la quinoa\nPreparar el pollo\nPreparar los vegetales\nArmar el bowl")
  print("Felicidades terminaste todas tus tareas")
 polainas = str(input("¿Quieres seguir con otra parte de la rutina? (SI/NO): ")).strip().lower()== "si"
 if not polainas:
  print("Gracias por usar el gestionador de tareas")
















  

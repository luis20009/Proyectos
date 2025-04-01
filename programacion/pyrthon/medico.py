
name= input("Ingrese su nombre:")
peso = float(input("Ingrese su peso"))
high = float(input("Ingrese su altura"))
IMC = peso/(high**2)
edad = int(input("Ingrese edad"))
Palts = float(input("Ingrese presion arteriar sistolica"))
Paltd = float(input("Ingrese presion arteriar diastolica"))
fumar = input("¿Fumas? (SI/No): ").strip().lower()
IMC = peso/(high**2)
def Clasificacion_Imc(IMC):
 if IMC < 18.5:
   return("Peso bajo")
 elif 18.5<IMC<25:
   return("Peso normal")
 elif 29<IMC:
   return("OBESIDAD")
def Clasificacion_pst(Palts, Paltd):
   if Palts<120 and Paltd<80:
      return("Normal")
   elif 129<Palts<120 and Paltd<80:
     return("elevada")
   elif Palts>=130 or Paltd>=80:
      return("Alta")

def recomendaciones(IMC, Palts, Paltd, edad, fumar):
    recomendaciones = []
    if IMC > 29 and Palts >= 130:
        recomendaciones.append("Es importante mantener un peso saludable y controlar su presión arterial.")
    if Palts >= 130:
        recomendaciones.append("Se recomienda que controle su presión arterial.")
    if edad >= 40 or fumar == "si" or Palts >= 129:
        recomendaciones.append("Es aconsejable que tome medidas para mejorar su salud general.")
    if fumar == "si":
        recomendaciones.append("Considera dejar de fumar para mejorar tu salud.")
    return recomendaciones

# Imprimir resultados y recomendaciones
print(f"\nResultados para {name}:")
print(f"IMC: {IMC:.2f} - {Clasificacion_Imc(IMC)}")
print(f"Presión arterial: {Clasificacion_pst(Palts, Paltd)}")

rec = recomendaciones(IMC, Palts, Paltd, edad, fumar)
if rec:
    print("\nRecomendaciones:")
    for pene in rec:
        print(f"- {pene}")
else:
   print("Tienes buena condicion fisica")


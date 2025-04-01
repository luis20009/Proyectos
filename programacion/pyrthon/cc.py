def obtener_datos():
    nombre = input("Ingrese su nombre: ")
    peso = float(input(f"Ingrese su peso {nombre}: "))
    altura = float(input(f"Ingrese su altura {nombre}: "))
    edad = int(input(f"Ingrese su edad {nombre}: "))
    p_arterial_sist = float(input(f"{nombre}, ingrese su presión arterial sistólica: "))
    p_arterial_dia = float(input(f"{nombre}, ingrese su presión arterial diastólica: "))
    fumar = input("¿Fumas? (SI/No): ").strip().lower()
    return nombre, peso, altura, edad, p_arterial_sist, p_arterial_dia, fumar

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificacion_imc(imc):
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def clasificacion_pst(p_sist, p_dia):
    if p_sist < 120 and p_dia < 80:
        return "Normal"
    elif 120 <= p_sist < 130 and p_dia < 80:
        return "Elevada"
    elif p_sist >= 130 or p_dia >= 80:
        return "Alta"

def recomendaciones(imc, p_sist, p_dia, edad, fumar):
    recomendaciones = []
    if imc > 29 and p_sist >= 130:
        recomendaciones.append("Es importante mantener un peso saludable y controlar su presión arterial.")
    if p_sist >= 130:
        recomendaciones.append("Se recomienda que controle su presión arterial.")
    if edad >= 40 or fumar == "si" or p_sist > 129:
        recomendaciones.append("Es aconsejable que tome medidas para mejorar su salud general.")
    if fumar == "si":
        recomendaciones.append("Considera dejar de fumar para mejorar tu salud.")
    return recomendaciones

# Ejecución del programa
nombre, peso, altura, edad, p_arterial_sist, p_arterial_dia, fumar = obtener_datos()
imc = calcular_imc(peso, altura)
clas_imc = clasificacion_imc(imc)
clas_pst = clasificacion_pst(p_arterial_sist, p_arterial_dia)
recs = recomendaciones(imc, p_arterial_sist, p_arterial_dia, edad, fumar)

print(f"Nombre: {nombre}")
print(f"IMC: {imc:.2f} - {clas_imc}")
print(f"Presión arterial: {clas_pst}")
print("Recomendaciones:")
for rec in recs:
    print(f"- {rec}")

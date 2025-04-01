from num2words import num2words

# Convertir un número a palabras en español
numero = int(input("Ingresa un número: "))
numero_en_palabras = num2words(numero, lang='es')  # 'lang="es"' asegura que el idioma sea español

print(f"El número {numero} en palabras es: {numero_en_palabras}")

          




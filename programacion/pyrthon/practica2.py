import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Interfaz Gráfica")
ventana.geometry("400x300")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, bienvenido a mi GUI!")
etiqueta.pack(pady=20)

# Crear un botón
def boton_click():
    etiqueta.config(text="¡Botón presionado!")

boton = tk.Button(ventana, text="Presióname", command=boton_click)
boton.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

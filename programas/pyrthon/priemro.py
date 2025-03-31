import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("silver")
t.speed(1)

def draw_pattern():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for i in range(36):
        t.color(colors[i % len(colors)])
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(70)

# Dibujar el patrón
draw_pattern()

# Ocultar la tortuga y mostrar la ventana
t.hideturtle()
turtle.done()

import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("Red")

    brad = turtle.Turtle()

    for i in range(0, 37):
        brad.shape("turtle")
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("Blue")
    #angie.circle(50)

    window.exitonclick()

draw_art()
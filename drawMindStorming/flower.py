import turtle

def draw_flower(petal_no, some_turtle, radius):
    degree_t = int(360/petal_no)
    print(degree_t)
    for petal_no in range(0, petal_no):
        some_turtle.circle(radius)
        some_turtle.right(degree_t)

def draw_art():
    window = turtle.Screen()
    shoe = turtle.Turtle()
    shoe.shape("turtle")
    shoe.color("Pink")
    draw_flower(5, shoe, 100)

    paper = turtle.Turtle()
    paper.shape("turtle")
    paper.color("Red")
    draw_flower(9, paper, 80)

    window.exitonclick()

draw_art()
from turtle import *

def fract(length, depth):
    if depth == 0:
        forward(length)
    else:
        fract(length/3, depth-1)
        right(60)
        fract(length/3, depth-1)
        left(120)
        fract(length/3, depth-1)
        right(60)
        fract(length/3, depth-1)

fract(500, 4)
from turtle import*
import turtle as t

def my_triflower():
     sides = str(80)
     loops = str(700)
     pen = 1
     for i in range(int(loops)):
         forward(i*2/int(sides)+i)
         left(10000/int(sides)+ .10000)
         hideturtle()
         pensize(pen)
         speed(50)

my_triflower()
t.done()

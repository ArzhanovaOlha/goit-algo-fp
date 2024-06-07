import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

turtle_draw = turtle.Turtle()
turtle_draw.shape("classic")
turtle_draw.color("#F102FD")

turtle_draw.speed(0)
colors = ['#CB02FE','#A401FE','#5801FF','#056BD7','#2DAFF3','#6BFFFF','black']

def draw_square(t, size):
  t.begin_fill()
  for i in range(4):
    
    t.forward(size)
    t.left(90)
  t.end_fill()
 

def draw_node(t, size, level,item):
  if item > 6:
    item = 0
  else:
    set_color = colors[item]
    if (level < 1):
      return
    else:
      draw_square(t, size)
          
      left_size = size * math.sqrt(3) / 2
      t.forward(size)
      t.left(90)
      t.forward(size)
      t.right(150)
      t.forward(left_size)
      t.left(90)
      t.color(set_color)
      draw_node(t, left_size, level - 1, item+1)

      right_size = size / 2
      t.right(180)
      t.forward(right_size)
      t.left(90)
      t.color(set_color)
      draw_node(t, right_size, level - 1,item+1)
      t.left(60)
      t.back(size)
      
turtle_draw.penup()
turtle_draw.goto(90, -150)
turtle_draw.left(90)
turtle_draw.pendown()

levels = int(input("Enter the number of levels: ")) 
draw_node(turtle_draw, 60, levels,0)

turtle_draw.hideturtle()

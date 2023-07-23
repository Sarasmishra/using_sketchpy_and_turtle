import turtle

win = turtle.Screen()
win.bgcolor("black")                         # for background color
#   my first turtle Shape

#      JUST REMOVE COMMENT TO USE THE CODE
'''
mine = turtle.Turtle()
mine.speed(10)
mine.shape("turtle")                        # for changing shape
mine.color("yellow","black")                # for line and arrow color
for i in range(0,300,10):
    mine.forward(300-i)
    mine.left(90)                           # it will rotate to left w.r.t angle
    mine.forward(300-i)
    mine.left(90)
    mine.forward(290-i)
    mine.left(90)
'''

#     USE OF CIRCLE METHOD
'''
t = turtle.Turtle()
t.color("blue")
t.speed(20)
for i in range(0,200,10):
    t.circle(200-i)
    t.circle(-200 + i)
for u in range(0,180,5):
    t.circle(180-i)
    t.circle(-180 + i)
for j in range(0, 100):
    t.circle(100 - j)
    t.circle(-100+j)
'''

# THIRD CANVAS
p = turtle.Turtle()
p.speed(20)
col =['red',"blue",'green','yellow','orange']
turtle.colormode(255)
for i in range(250):
    p.color(col[i%5])
    p.pensize(i/40+1)
    p.forward(i)
    p.left(69)







import turtle
d=turtle.Turtle()
d.pensize(4)
d.speed(3)

def move():
    d.up()
    d.goto(x,y)
    d.down()
    
for i in range(24):
    d.color("blue")
    d.forward(80)
    d.backward(80)
    d.left(15)

d.up()
d.goto(0,-80)
d.down()

d.circle(80,360)

d.begin_fill()
d.color("green")
d.forward(350)
d.backward(700)
d.right(90)
d.forward(160)
d.left(90)
d.forward(700)
d.left(90)
d.forward(160)
d.end_fill()

d.up()
d.goto(-350,80)
d.down()
d.begin_fill()
d.color("orange")
d.forward(160)
d.right(90)
d.forward(700)
d.right(90)
d.forward(160)
d.right(90)
d.forward(700)
d.end_fill()

turtle.done()

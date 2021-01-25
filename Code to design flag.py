import turtle
t= turtle.Turtle()
t.pensize(4)
t.speed(10)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#for Ashok Chakra
# 24 strokes
# 350/24 = 15degree

t.color("#054188")
for i in range(24): # cuz we need 24 strokes
    t.forward(80)
    t.backward(80)
    t.left(15)

move(0,-80) #moving to Y axis
t.circle(80,360) #360 full circle80 pixels

#for Green color
#moving 90 degree to right
t.begin_fill() #filling it with green color
t.color("green")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

# for Orange part
t.begin_fill()
t.color("orange")
move(-350,80)
t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()





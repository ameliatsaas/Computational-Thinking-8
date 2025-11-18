import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed(0)
t1.goto(0,0)



turtle.Screen() .bgcolor("black")


colors = ["medium slate blue", "plum", "indigo"]
for i in range(200):
    t1.color( colors[ i % 3] )
    t1.forward(1+i)
    t1.left(67)
    t1.forward(1+i)
    t1.left(45)
t1.penup()
t1.goto(-100000,0)

    

turtle.exitonclick()
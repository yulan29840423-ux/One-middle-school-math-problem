import turtle
def backorigin():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
turtle.speed(100)
backorigin()
turtle.goto(0, -400)
backorigin()
turtle.goto(0, 400)
backorigin()
turtle.goto(400, 0)
backorigin()
turtle.goto(-400, 0)
turtle.penup()

A=0
B=0
for A in range(0,25):
    for B in range(0,20):
        if 120*A=150*B==3000:
            print('solution'+'A='+str(A     )+'B='+str(B))
            s_A=A*15
            s_B=B*15
            turtle.goto(s_A,s_B)
            turtle.pendown()
            turtle.dot(10,"red")
            turtle.penup()
turtle.done()
 
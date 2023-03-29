import turtle

def draw_return():
    s = turtle.getscreen()
    t = turtle.Turtle()
    c = t.clone()
    n = c.clone()
    b = n.clone()
    turtle.title("Yaretzi's Turtle")
    turtle.bgcolor("pink")
    t.shape("turtle")
    t.color("black")
    t.penup()
    t.backward(10)
    t.pendown()
    t.pen(fillcolor="black", pensize=10)
    t.begin_fill()
    t.dot(400)
    t.end_fill()
    c.color("blue")
    c.dot(300)
    n.color("red")
    n.dot(200)
    b.color("yellow")
    b.dot(100)
def draw_heart():
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.title("Yaretzi's Turtle")
    turtle.bgcolor("black")
    t.shape("turtle")
    t.pencolor("red")
    t.color("red")
    t.pensize(3)
    t.rt(50)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.setheading(0)
    t.lt(50)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.lt(135)
    t.backward(80)
    t.begin_fill()
    t.lt(45)
    t.fd(125)
    t.rt(100)
    t.fd(125)
    t.rt(180)
    t.fd(20)
    t.lt(45)
    t.fd(30)
    t.end_fill()
def draw_tree():
    #Background info
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.title("Yaretzi's Turtle")
    turtle.bgcolor("blue")
    t.shape("turtle")
    
    #Trunk
    t.pencolor("brown")
    t.fillcolor("brown")
    t.begin_fill()
    t.backward(80)
    t.lt(90)
    t.backward(100) 
    t.rt(90)
    t.fd(80)
    t.lt(90)
    t.fd(100)
    t.end_fill()
    
    #Right side of tree
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    t.lt(90)
    t.fd(150)
    t.rt(180)
    t.fd(200)
    for x in range(4):
        t.lt(110)
        t.fd(70)
        t.rt(105)
        if x !=3:
            (t.fd(50))      
    t.lt(110)
    t.fd(75)
    
    #Left side of tree
    t.lt(100)
    t.fd(190)
    t.rt(210)
    t.fd(40)
    t.lt(210)
    t.fd(90)
    t.rt(210)
    t.fd(60)
    t.lt(210)
    t.fd(90)
    t.rt(210)
    t.fd(60)
    t.lt(210)
    t.fd(133)
    t.end_fill()
    
    

    
import time
def main():
    print("main")
      
if __name__ == '__main__':
    main()
    print("Yaretzi")
    print("hello world")
    #draw_return()
    #draw_heart()
    draw_tree()
    turtle.exitonclick()
    



      

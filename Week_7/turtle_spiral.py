#Making a Spiral Using Turtle
import turtle

turtle.bgcolor('black')
spiral = turtle.Turtle()



dot_distance=24

spiral.setpos(-250,250)
spiral.penup()

def spiral_turtle(m,n):
    k,l=0,0
    f=0
    spiral.color('white')

    while k<m and l<n:
        if f==1:
            spiral.right(90)

        for i in range(l,n):
            spiral.dot()
            spiral.forward(dot_distance)

        k+=1
        f=1
        spiral.right(90)
        for i in range(k,m):
            spiral.dot()
            spiral.forward(dot_distance)
        
        n -= 1

        spiral.right(90)

        if k<m:
            for i in range(n-1,l-1,-1):
                spiral.dot()
                spiral.forward(dot_distance)
            m -= 1
        spiral.right(90)
        if l<n:
            for i in range(m-1,k-1,-1):
                spiral.dot()
                spiral.forward(dot_distance)
            l+=1

spiral_turtle(20,20)
turtle.done()
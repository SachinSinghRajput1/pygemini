from turtle import *
colors = [ "red" , "cyan" , "green" , "yellow" , "white" , "orange"]
bgcolor("black") 
speed(100)
for x in range(400):
       pencolor(colors[x%6])
       width(x/100+3)
       forward(x)
       left(99)
       
hideturtle()

done()
    
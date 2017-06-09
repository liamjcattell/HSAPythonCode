# Turtle graphics example, drawing an n-gon
import turtle

bob = turtle.Turtle()

n = int(input("How many sides does the polygon have? "))

for i in range(0,n):
	bob.forward(50)
	bob.left(180 - (n-2)*180/n)
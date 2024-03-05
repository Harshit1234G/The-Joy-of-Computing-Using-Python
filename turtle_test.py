import math 
import turtle


t = turtle.Turtle()

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) -5 * math.cos(2*k) -2 * math.cos(3*k) - math.cos(4*k)

t.speed("fastest")
turtle.bgcolor("black")
t.color("#f73487")

for i in range(720):
    t.goto(hearta(i) * 20, heartb(i) * 20)
    t.goto(0,0)

turtle.mainloop()
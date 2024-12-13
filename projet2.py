from turtle import *

t = Turtle()
t.setpos(0,0)
t.goto(0,-100)
t.goto(0,100)
t.goto(0,0)
t.goto(-100,0)
t.goto(100,0)
i = 0

def fonctionLineaireCanV():
    print("Vous avez choisi la fonction linéaire sous la forme y = ax+b!")
    global a
    a = input("Quelle est la valeur de a?:")
    a = int(a)
    global b
    b = input("Quelle est la valeur de b?:")
    b = int(b)

def fonctionLineaireCan(x):
   return a*x+b

fonctionLineaireCanV()

for i in range(-100, 100):
    t.color("black")
    t.goto(i,fonctionLineaireCan(i))
        

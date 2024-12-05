from turtle import *

t = Turtle()
t.setpos(0,0)
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



while True:

   for i in range(100):
    t.color("red")
    t.goto(i,10*fonctionLineaireCan(i))
    

    for i in range(100):
        t.color("black")
        t.goto(i,10*a*i)
        

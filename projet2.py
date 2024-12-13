from turtle import *

t = Turtle()
t.setpos(0,0)
t.goto(0,-100)
t.goto(0,100)
t.goto(0,0)
t.goto(-100,0)
t.goto(100,0)
i = 0


a = 0
b = 0
c = 0
Go = 0

def choixFonction():
    global Go
    print("Quelle fonction voulez-vous utiliser?")
    print("1. Fonction lineaire canonique (y = ax+b)")
    print("2. Fonction quadratique canonique (y = ax^2+bx+c)")

    reponse = input("Entrez votre choix: ").capitalize()
    match reponse:
        case ("FONCTION LINEAIRE CANONIQUE" | "1"):
            fonctionLineaireCanValeur()
           

        case _:
            print("Choix invalide! Veuillez réessayer, le nombre ou le nom de la fonction.")
            choixFonction()
    Go = 1
    
def fonctionLineaireCanValeur():
    global a
    global b
    print("Vous avez choisi la fonction linéaire sous la forme y = ax+b!")
    a = input("Quelle est la valeur de a?:")
    a = int(a)
    b = input("Quelle est la valeur de b?:")
    b = int(b)

def fonctionLineaireCan(x):
   global a
   global b
   return a*x + b

def fonctionQuadratiqueCanValeur(x):
    print("Vous avez choisi la fonction quadratique sous la forme y = ax^2+bx+c!")

choixFonction()
print(Go)
t.color("black")
if Go == 1:
    t.pendown()
    for i in range(-100, 100):
        t.goto(i,fonctionLineaireCan(i))
        
        
t.screen.mainloop()        

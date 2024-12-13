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
    print("Vous avez choisi la fonction linéaire sous la forme y = ax+b!")
    a = input("Quelle est la valeur de a?:")
    a = int(a)
    b = input("Quelle est la valeur de b?:")
    b = int(b)

def fonctionLineaireCan(x):
   return a*x+b

def fonctionQuadratiqueCanValeur(x):
    print("Vous avez choisi la fonction quadratique sous la forme y = ax^2+bx+c!")

choixFonction()
print(Go)
if Go == 1:
    for i in range(-100, 100):
        t.color("black")
        t.goto(i,fonctionLineaireCan(i))
        
t.screen.mainloop()        

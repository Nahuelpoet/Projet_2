from turtle import *

t = Turtle()


a = 0
b = 0
c = 0
Go = 0
fonction = 0
t.color("black")

def choixFonction():
    global Go
    global fonction
    print("Quelle fonction voulez-vous utiliser?")
    print("1. Fonction lineaire canonique (y = ax+b)")
    print("2. Fonction quadratique canonique (y = ax^2+bx+c)")

    reponse = input("Entrez votre choix(entrer le numéro de la fonction): ")
    match reponse:
        case ("1"):
            print("Vous avez choisi la fonction linéaire sous la forme y = ax+b!")
            fonction = 1
            ValeurLineaire()

        case ("2"):
            print("Vous avez choisi la fonction quadratique sous la forme y = ax^2+bx+c!")
            fonction = 2
            ValeurLineaire()
        
        case _:
            print("Choix invalide! Veuillez réessayer le nombre de la fonction.")
            choixFonction()
    Go = 1
    
def ValeurLineaire():
    global a
    global b
    global c
    a = input("Quelle est la valeur de a? ATTENTION, le code plante si vous n'écrivez pas un nombre (négatif ok):")
    a = float(a)
    b = input("Quelle est la valeur de b? ATTENTION, le code plante si vous n'écrivez pas un nombre (négatif ok):")
    b = float(b)
    if fonction == 2:
        c =input("Quelle est la valeur de c? ATTENTION, le code plante si vous n'écivez pas un nombre (négatif ok):")
        c = float(c)


def fonctionLineaireCan(x):
   global a
   global b
   return a*x + b

def fonctionQuadratiqueCan(x):
    global a
    global b
    global c
    return a*x**2 + b*x + c

choixFonction()

range = 1
range = input("Quelle sont les valeurs de x que vous voulez afficher? Metter seulement la valeur absolue de x:")
range = int(range)
if range <= 0:	
    range = input("Valeur invalide! Veuillez entrer une valeur positive:")
    range = int(range)
if range > 100:
    range = input("Valeur invalide! Veuillez entrer une valeur inférieure à 100:")
    range = int(range)

if range < 30:
    range = range *10

global rangenegatif
rangenegatif = -range
global rangepositif
rangepositif = range

t.setpos(0,0)
t.goto(0,-range)
t.goto(0,range)
t.goto(0,0)
t.goto(-range,0)
t.goto(range,0)



if Go == 1 and fonction == 1:
        i = 0
        t.penup()
        while i > -range:
            if fonctionLineaireCan(i) < range and fonctionLineaireCan(i) > -range:
                i = i-1

            else:
                rangenegatif = i
                break

        while i < range:
            if fonctionLineaireCan(i) < range and fonctionLineaireCan(i) > -range:
                i = i+1

            else:
                rangepositif = i
                break

        print(rangenegatif)
        print(rangepositif)
        t.pendown()
        i = 0
        while i < rangepositif:
            t.penup()
            t.goto(i,fonctionLineaireCan(i))
            t.pendown()
            i = i + 1
        i = 0
        while i > rangenegatif:
            t.penup
            t.goto(i,fonctionLineaireCan(i))
            t.pendown
            i = i -1

if Go == 1 and fonction == 2:

        i = 0
        t.penup()

        while i < range:
            if a > 0 and fonctionQuadratiqueCan(range - i) > range:
                i = i+1

            elif a < 0 and fonctionQuadratiqueCan(range - i) < -range:
                i = i+1

            else:
                t.setpos(-(range - i),fonctionQuadratiqueCan(-(range - i)))
                rangenegatif = -(range - i)
                break
        while i < range:
            if fonctionQuadratiqueCan(-range + i) < -range:
                i = i+1

            else:
                rangepositif = range - i
                break

        range = i
        t.pendown()
        i = 0
        while i < rangepositif:
            t.penup()
            t.goto(i,fonctionQuadratiqueCan(i))
            t.pendown()
            i = i + 1
        while i > rangenegatif:
            t.penup
            t.goto(i,fonctionQuadratiqueCan(i))
            t.pendown
            i = i -1
        
        
t.screen.mainloop()        

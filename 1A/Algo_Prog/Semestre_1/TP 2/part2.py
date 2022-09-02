from turtle import right, color, end_fill, begin_fill, backward, goto, circle, position, done, penup, setx, sety, pendown, left, forward

def drawRectangle(largeur:float, hauteur:float, posx:float = 0, posy: float = 0, fill:bool = False):
    penup()
    setx(posx)
    sety(posy)
    pendown()
    if(fill) : begin_fill()
    for i in range (2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    penup()
    if(fill) :
        color("white") 
        end_fill()
        color("black")

def drawCircle(rayon:float, posx:float = 0, posy:float = 0, half: float = 360):
    penup()
    setx(posx)
    sety(posy)
    pendown()
    circle(rayon, half)
    penup()

if __name__ == "__main__":
    #mur maison
    drawRectangle(150, 100)
    #porte
    drawRectangle(15, 30, 75)
    #arc de cercle au dessus de la porte
    forward(15)
    left(90)
    forward(30)
    drawCircle(7.5, position()[0], position()[1], half = 180)
    #poignée 
    forward(15)
    left(90)
    forward(5)
    drawCircle(2, position()[0], position()[1])

    #fenetre gauche
    drawRectangle(20, 30, 20, 60)
    drawRectangle(20, 30, 40, 60)
    #fenetre droite
    drawRectangle(20, 30, 100, 60)
    drawRectangle(20, 30, 120, 60)

    #pente gauche
    setx(0)
    sety(100)
    forward(40)
    left(90)
    pendown()
    forward(50)
    goto((0, 100))
    penup()

    #pente droite
    setx(150)
    sety(100)
    pendown()
    goto((110, 150))
    backward(50)
    penup()

    #dessus du toit
    forward(50)
    pendown()
    left(90)
    forward(70)

    #cheminée
    drawRectangle(10, 20, 60, 160, True)

    #fumée

    #1
    penup()
    backward(5)
    left(-90)
    forward(10)
    drawCircle(3, position()[0], position()[1])
    #2
    forward(5)
    right(90)
    forward(5)
    drawCircle(2.5, position()[0], position()[1])

    #3
    forward(10)
    right(-90)
    forward(5)
    drawCircle(2, position()[0], position()[1])

    #Soleil
    drawCircle(15, 150, 180)
    done()
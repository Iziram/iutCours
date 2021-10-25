import turtle

def square(largeur: int ):
    turtle.setheading(0)
    for i in range(4):
        turtle.fd(largeur)
        turtle.left(-90) 

def generator(coords:tuple, largeur:int, reduction: int = 10) -> int:
    turtle.penup()
    turtle.setx(coords[0])
    turtle.sety(coords[1])
    turtle.pendown()
    count:int = 0
    while largeur >= reduction:
        square(largeur)
        largeur -= reduction
        count += 1

if __name__ == "__main__":
    generator((-50,50), 200)
    turtle.done()    
import turtle, gestionSaisi
def controleTortue():
    turtle.setpos(0, 0)
    c:str = ""
    while c != 'q':
        c = gestionSaisi.recupcar()
        if c == "o":
            turtle.setheading(90)
            turtle.fd(10)
            
        elif c == "k":
            turtle.setheading(180)
            turtle.fd(10)
            
        elif c == "m":
            turtle.setheading(0)
            turtle.fd(10)
        elif c == "l":
            turtle.setheading(-90)
            turtle.fd(10)
        
    
if __name__ == "__main__":
    controleTortue()
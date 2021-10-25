
def getLongeur(x:str, y:str):
    l : float = float(input(f"longeur {x}{y}: "))
    triangle[x+y] = l

def verifTriangleRectangle() -> bool:
    ab_s = triangle["AB"] ** 2
    bc_s = triangle["BC"] ** 2
    ac_s = triangle["AC"] ** 2
    return ac_s ** 0.5 == (ab_s+bc_s)**0.5

def cos(adjacent:float, hypothenuse:float) -> float:
    return adjacent/hypothenuse
def sin(oppose:float, hypothenuse:float) -> float:
    return oppose/hypothenuse

if __name__ =="__main__":
    triangle : dict = {}
    getLongeur("A","B")
    getLongeur("B","C")
    getLongeur("A","C")

    if not verifTriangleRectangle:
        print("Le triangle n'est pas rectangle.")
    else:
        angle : str = input("Angle A ou Angle C: (A ou C) ").capitalize()
        if angle == "A":
            print(f'cos(A) = {cos(triangle["AB"], triangle["AC"])}')
            print(f'sin(A) = {sin(triangle["BC"], triangle["AC"])}')
        elif angle == "C":
            print(f'cos(C) = {cos(triangle["BC"], triangle["AC"])}')
            print(f'sin(C) = {cos(triangle["AB"], triangle["AC"])}')
        else:
            print("Angle invalide.")
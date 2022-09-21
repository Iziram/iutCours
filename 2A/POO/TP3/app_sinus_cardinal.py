from math import sin


def sinus_cardinal(x):
    try:
        return sin(x) / x
    except ZeroDivisionError:
        print("Division par 0 impossible retour avec 1")
        return 1


if __name__ == "__main__":
    liste_sinus = []
    for i in [x / 10.0 for x in range(-30, 35, 5)]:
        liste_sinus.append((i, sinus_cardinal(i)))
    print(liste_sinus)

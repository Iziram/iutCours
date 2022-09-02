# Le Msb : positif ou négatif et le Lsb : impair ou pair

import numpy as np




if __name__ == "__main__":
    # #---1---
    # number = np.int8(int(input("nombre: ")))
    # b = number & 0b10000001 == 1
    # print(b)
    # #---2---
    # a = input("escape : ")
    # for i in ["4","<","T","]","q","["," ", a]:
    #     caractere = ord(i)
    #     b = not ( ( caractere > 47 and caractere < 58 ) or ( caractere > 64 and caractere < 91) or (caractere > 96 and caractere < 123) )
    #     print(f'b={b} | i= {i} | caractere={caractere}')
    # #---3---

    for a in [8,64, 149, 122, 175]:
        print(f'{( a & 0b01000000) >> 6} | {( a & 0b00010000) >> 4}')
        b = ( a & 0b01000000) >> 6 == 1 or ( a & 0b00010000) >> 4 == 0 
        print(f'b={b} | bin = {bin(a)} | a = {a}')
    pass
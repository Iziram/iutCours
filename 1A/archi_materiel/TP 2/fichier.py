import numpy as np
from definitions import *

def integer(c:str) -> int:
    if type(c) == int : return c
    if '0x' in c: return int(c,16)
    if '0b' in c: return int(c,2)
    if '0o' in c: return int(c,8)
    if c in "abcdefghijklmnopqrstuvwxyz": return int(ord(c))
    else : return int(c)

def fonc(c:str, signed:bool = False):
    print(f"-------{c}-------")
    if signed : a : np.uint8 = np.uint8(c)
    else : a : np.int8 = np.int8(c)
    print(a)
    print(hex(a))

# for i in ["0b1101","0xf4","223","0o223",ord("A"),ord("A")+32, "-28","1000"]:
#     fonc(i)

for i in ["0b1101", "0b11111101", "a","-28","0xf1","1000"]:
    fonc(i, True)

#Résultats unsigned
# -------0b110-------
# 6
# 0x6
# -------0xf4-------
# 244
# 0xf4
# -------223-------
# 223
# 0xdf
# -------0o223-------
# 147
# 0x93
# -------65-------
# 65
# 0x41
# -------97-------
# 97
# 0x61
# --------28-------
# 228
# 0xe4
# -------1000-------
# 232
# 0xe8



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def dec2bin(d,nb):
    """Représentation d'un nombre entier en chaine binaire (nb: nombre de bits du mot)"""
    if d == 0:
        return "0".zfill(nb)
    if d<0:
        d += 1<<nb
    b=""
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)

def dec2hex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))




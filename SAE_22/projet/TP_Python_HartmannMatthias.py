#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:31:27 2022

@author: romuald
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

plt.close('all')


############################################################################
def spectre(signal):
    Fourier = 2/(len(signal))*np.fft.fftshift(np.fft.fft(signal,int(1000)))
    Module = np.abs(Fourier)
    Module1=Module[int(len(Module)/2):len(Module)]
    return Module1

def affichage(t,signal,titre):
    plt.figure()
    plt.plot(t,signal)
    plt.grid()
    if t[len(t)-1]<100:
        plt.xlabel('temps en s', fontsize=14)
    else :
        plt.xlabel('fréquence en Hz ', fontsize=14)
    plt.ylabel('Amplitude en V', fontsize=14)
    plt.title(titre, fontsize=16)
    plt.show()


def filtre(ordre, fc, typef,entree ):
    if typef=='band':
        fcb=fc[0]/(fe/2)
        fch=fc[1]/(fe/2)
        b, a = scipy.signal.butter(ordre, [fcb,fch], btype=typef, analog=False)
        w, h = scipy.signal.freqz(b, a)
        f=0.5 * fe * w / np.pi
        fig, ax = plt.subplots(1,1, figsize = (15, 10))
        plt.grid()    
        ax.semilogx(f[1:len(f)-1], 20*np.log10(abs(h[1:len(f)-1])),linewidth = 2)
        ax.set_xlim([10,fe/2])
        ax.set_ylim([-65,5])
        ax.xaxis.set_tick_params(labelsize=12)
        ax.yaxis.set_tick_params(labelsize=12)
        ax.set_title('Gain en dB du filtre', fontsize=14)
        ax.set_xlabel('Fréquence, échelle semilog', fontsize=14)
        ax.set_ylabel('20log|G| en dB', fontsize=14)
        ax.grid(True, which="both")
        
        #Notation de la fréquence de coupure à -3dB
        ax.vlines(x=fc[0], ymin=-65, ymax=-3, colors='g',linestyles='dashed')
        ax.vlines(x=fc[1], ymin=-65, ymax=-3, colors='g',linestyles='dashed')
        ax.hlines(y=-3, xmin=1, xmax=fc[1], colors='g',linestyles='dashed')
        #ax.text(8.5, -5.5, 'G à fc', fontsize=16)
    
    else :
        fcn=fc/(fe/2)
        b, a = scipy.signal.butter(ordre, fcn, btype=typef, analog=False)
        w, h = scipy.signal.freqz(b, a)
        f=0.5 * fe * w / np.pi
        fig, ax = plt.subplots(1,1, figsize = (15, 10))
        plt.grid()    
        ax.semilogx(f[1:len(f)-1], 20*np.log10(abs(h[1:len(f)-1])),linewidth = 2)
        ax.set_xlim([10,fe/2])
        ax.set_ylim([-65,5])
        ax.xaxis.set_tick_params(labelsize=12)
        ax.yaxis.set_tick_params(labelsize=12)
        ax.set_title('Gain en dB du filtre', fontsize=14)
        ax.set_xlabel('Fréquence, échelle semilog', fontsize=14)
        ax.set_ylabel('20log|G| en dB', fontsize=14)
        ax.grid(True, which="both")
        
        #Notation de la fréquence de coupure à -3dB
        ax.vlines(x=fc, ymin=-65, ymax=-3, colors='g',linestyles='dashed')
        ax.hlines(y=-3, xmin=1, xmax=fc, colors='g',linestyles='dashed')
        #ax.text(8.5, -5.5, 'G à fc', fontsize=16)
    
    
    
    #Gère l'espacement vertical entre les 2 systèmes d'axes
    fig.tight_layout()
    out=scipy.signal.lfilter(b, a, entree)
    return out

def sinus(a, f, t):
    return a * np.sin(2*np.pi*f*t)
def cosinus(a, f, t):
    return a * np.cos(2*np.pi*f*t)
#############################################################################
fe=10000
T=0.06

t = np.linspace(0,T-1/fe,int(T*fe))
f=np.linspace(0,fe/2-1/500,int(500))

# Partie 2.1
modulant = sinus(1, 100, t)
affichage(t, modulant, "Modulant")
"""

Le signal affiché correspond bien au signal "Modulan" entré.
Il y a bien un motif qui dure 0.01 secondes et l'amplitude va bien de 1V à -1V

"""

affichage(f, spectre(modulant), "Spectre du modulant")

""" 
Le spectre est bien représenté, 
on y voit une seule raie en f = 100Hz et qui a pour valeur 1V
"""

#Partie 2.2

porteuse = cosinus(1, 1000, t)

module = modulant * porteuse

affichage(t, porteuse, "Affichage de la porteuse")
affichage(f, spectre(porteuse), "Affichage de la porteuse")
affichage(t, module, "Affichage du module")
affichage(f, spectre(module), "Affichage du module")

"""
Le spectre du module généré correspond bien au spectre théorique.
On retrouve bien 2 raies centrée autour de fe et ayant pour fréquence :
fe - fm et fe +fm
Leur amplitude étant 0.5 V.
"""

#Partie 3.1
demod = module * porteuse

affichage(t, demod, "Affichage du module multiplé par la porteuse")
affichage(f, spectre(demod), "Affichage du module multiplé par la porteuse")
""" 
Niveau temporel : l'amplitude du signal est 1V/-1V
Niveau fréquentiel : 
    Il y a 3 raies :
        1ere raie : f= 100Hz A = 0,5V
        2eme raie : f= 1900Hz A = 0.25V
        3eme raie : f= 2100Hz A = 0.25V

Cela correspond à la théorie, nous avons bien une raie 
correspondant à la raie du modulant et 2 raies déplacés du double de la porteuse.
"""

#Partie 3.2

sortie = filtre(4, 200, "low", demod)

affichage(f, spectre(sortie), "Spectre du signal de sortie")
"""
1 seule raie, avec f = 100Hz et A = 0.5

Le passe bas garde alors la raie correspondant au signal modulant et retire les 
fréquences correspondantes à l'échantillonage
"""

affichage(t, sortie, "Affichage du signal de sortie")
affichage(t, modulant, "Affichage du signal de sortie")
"""
Les signaux sont quasiment identiques. Seul l'amplitude change, 
0.5V/-0.5V pour le signal de sortie
1V/-1V pour le signal modulant
"""

#Partie 4

modulant = sinus(0.5, 100, t)
porteuse = cosinus(1, 1000, t)

module = (1 + modulant) * porteuse
affichage(f, spectre(module), "Affichage du spectre du signal modulé")
demod = module * porteuse
sortie = filtre(2, [90,200], "band", demod)
affichage(f, spectre(sortie), "Affichage du spectre du signal modulé")

affichage(t, modulant, "Affichage du signal d'origine")
affichage(t, sortie, "Affichage du signal de sortie")

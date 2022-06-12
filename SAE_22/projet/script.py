#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:31:27 2022

@author: romuald
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from scipy.io.wavfile import write
from scipy.io import wavfile
plt.close('all')

############################################################################




def spectre(signal):
    Fourier = 2/len(signal)*np.fft.fftshift(np.fft.fft(signal,int(2*len(signal))))
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
        ax.set_title('Gain en dB du filtre', fontsize=16)
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
        ax.set_title('Gain en dB du filtre', fontsize=16)
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
#############################################################################


# importation du fichier son
fe, mod = wavfile.read("matthias.wav")
T=len(mod)/fe

t = np.linspace(0,T-1/fe,int(T*fe))
f=np.linspace(0,fe/2-1/len(mod),int(len(mod)))

""" == Partie 2.2 : Importation sous python == """
# incompréhension ici, mon fichier à toutes les caractéristiques d'un fichier wav 24 bit PCM et fe = 22050Hz
# néanmoins je dois diviser mon signal par 2**31 au lieu de 2**23
signal = np.divide(mod, 2**31) 


# affichage(t,signal,"signal temporel échantillonné")

# affichage(f, spectre(signal), 'spectre du signal échantillonné')

signal_filtre = filtre(7, 3000, 'low', signal)
# affichage(f,spectre(signal_filtre), 'spectre du signal échantillonné et filtré')

""" == Partie 2.3 : Transposition de fréquence == """

signal_porteur = np.cos(2*np.pi*3307*t)
signal_transporte = np.multiply(signal_porteur, signal_filtre)

""" Affichage du signal porteur """
# affichage(t, signal_porteur, 'Signal temporel porteur')
# affichage(f, spectre(signal_porteur), 'spectre du signal porteur')

""" Affichage du signal transporté """
# affichage(t, signal_transporte, 'Signal temporel transporté')
# affichage(f, spectre(signal_transporte), 'spectre du signal transporté')


""" == Partie 2.4 : Démodulation == """

signal_demodule = np.multiply(signal_transporte, signal_porteur)
signal_demodule_filtre = filtre(7, 3000, 'low', signal_demodule)

""" Affichage du signal demodulé """
affichage(t, signal_demodule, 'Signal temporel démodulé')
affichage(f, spectre(signal_demodule), 'spectre du signal démodulé')

""" Affichage du signal demodulé et filtré """
affichage(t, signal_demodule_filtre, 'Signal temporel démodulé et filtré')
affichage(f, spectre(signal_demodule_filtre), 'spectre du signal démodulé et filtré')


""" == Partie 2.5 : Ecoute du son == """
write('final.wav',fe,signal_demodule_filtre)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:26:42 2020

@author: guilhermearanha
"""

print('Bem vindo ao SUPER CRAPS DO ARANHA')

while 1:
    try:
        banco = int(input('Quantas fichas você tem?\n'))
        break
    except:
        print('Um número inteiro, por favor...\n')
        
fase = 1
resposta = ''

while banco > 0:
    
    if fase == 1:   #inicio da fase come out
        print('\n∆ Está iniciado o Come Out ∆')
        print('Gostaria de fazer alguma aposta? (s/n)')
        while 1:    #pergunta se quer ou nao fazer uma aposta
            resposta = input()
            resposta = resposta.lower()
            if resposta == 's' or resposta == 'n' or resposta == 'sim' or resposta == 'não':
                break
            else:
                print('?')
        
        








    break
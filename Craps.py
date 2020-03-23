#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:26:42 2020

@author: guilhermearanha
"""

def inputInteiro():
    while 1:
        try:
            n = int(input())
            break
        except:
            print('?')
    return n




print('Bem vindo ao SUPER CRAPS DO ARANHA')

while 1:
    try:
        banco = int(input('Quantas fichas você tem?\n'))
        break
    except:
        print('\nUm número inteiro, por favor...\n')
        
fase = 1
resposta = ''

plb = 0
f = 0
ac = 0
t = 0

while banco > 0:
    
    if fase == 1:   #inicio da fase come out
        print('\n∆ Está iniciado o Come Out ∆')
        print('Gostaria de fazer alguma aposta? (s/n)')
        
        while 1:    #loop de apostas
            while 1:    #quer ou nao fazer uma aposta
                resposta = input('')
                resposta = resposta.lower()
                if resposta == 's' or resposta == 'n' or resposta == 'sim' or resposta == 'não':
                    break
                else:
                    print('?')
            
            if resposta == 'n' or resposta == 'não':
                break
        
            if resposta == 's' or resposta == 'sim':    #se sim, qual aposta?
                print('\nQual? (Pass Line Bet(plb) / Field(f) / Any Craps(ac) / Twelve(t) / Não quero mais apostar(x))')
                while 1:
                    resposta = input()
                    resposta = resposta.lower()
                    if resposta == 'pass line bet' or resposta == 'plb' or resposta == 'field' or resposta == 'f' or resposta == 'any craps' or resposta == 'ac' or resposta == 'twelve' or resposta == 't' or resposta == 'x':
                        break
                    else:
                        print('?')
                
                if resposta == 'x':
                    break
                        
                print('\nQuanto você gostaria de apostar?')
                while 1:
                    aposta = inputInteiro()
                    if aposta > banco:
                        print('\nVocê não tem ' + str(aposta) + ' fichas!')
                    else:
                        banco -= aposta
                        break
                
                if resposta == 'pass line bet' or resposta == 'plb':
                    plb += aposta
                elif resposta == 'field' or resposta == 'f':
                    f += aposta
                elif resposta == 'any craps' or resposta == 'ac':
                    ac += aposta
                elif resposta == 'twelve' or resposta == 't':
                    t += aposta
                else:
                    print('Há algo de errado no programa')
                
                print('\nGostaria de fazer mais alguma aposta? (s/n)')
        
        print(plb)
        print(f)
        print(ac)
        print(t)










    break
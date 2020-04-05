#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:26:42 2020

@author: guilhermearanha
"""
import random

def inputInteiro(): #funcao para receber no input um numero inteiro
    while 1:
        try:
            n = int(input())
            if n >= 0:
                break
        except:
            print('?')
    return n

def printDados():   #funcao para mostrar os dados aleatoriamente organizados
    texto = '\n'
    for i in range(4, random.randint(5,10)):
        texto += ' '
    texto += '[' + str(dadoA) + ']'
    if random.randint(0,1) == 1:
        texto += '\n'
    for i in range(4, random.randint(5,10)):
        texto += ' '
    texto += '[' + str(dadoB) + ']'
    print(texto + '\n')
    


print('Bem vindo ao SUPER CRAPS DO ARANHA')

while 1:    #input quantas fichas vc tem
    try:
        banco = int(input('Quantas fichas você tem?\n'))
        if banco > 0:
            break
    except:
        print('\nUm número inteiro positivo, por favor...\n')
        
fase = 1    #declara todas as variaveis que seram usadas
dadoA = 0
dadoB = 0
soma = 0
somaplb = 0
resposta = ''

plb = 0
f = 0
ac = 0
t = 0

while 1:    #loop de fases
    
    if fase == 1:   #inicio da fase específica
        print('\n∆ Está iniciado o Come Out ∆')
    if fase == 2:
        print('\n∫ Está iniciado o Point ∫')
    print('Gostaria de fazer alguma aposta? (s/n)')
    
    while 1:    #loop de apostas
        while 1:    #quer ou nao fazer uma aposta
            resposta = input('')
            resposta = resposta.lower()
            if resposta == 's' or resposta == 'n' or resposta == 'sim' or resposta == 'não':
                break
            else:
                print('?')
        
        if resposta == 'n' or resposta == 'não':    #se a resposta for não, ou o jogo continua com as apostas ja feitas ou se não houverem apostas feitas ele pergunta se vc quer sair ou não
            if plb + f + ac + t == 0:
                print('\nQuer mesmo sair do jogo? (s/n)')
                while 1:    #quer sair ou não
                    resposta = input('')
                    resposta = resposta.lower()
                    if resposta == 's' or resposta == 'n' or resposta == 'sim' or resposta == 'não':
                        break
                    else:
                        print('?')
                if resposta == 's' or resposta == 'sim':
                    print('\nVocê saiu do jogo com ' + str(banco) + ' fichas')
                    break
                else:
                    print('\nGostaria de fazer alguma aposta? (s/n)')
            else:
                break
    
        if resposta == 's' or resposta == 'sim':    #se sim, qual aposta?
            
            if fase == 1:   #opcoes de aposta na fase come out
                print('\nQual? (Pass Line Bet(plb) / Field(f) / Any Craps(ac) / Twelve(t) / Não quero mais apostar(x))')
                while 1:
                    resposta = input()
                    resposta = resposta.lower()
                    if resposta == 'pass line bet' or resposta == 'plb' or resposta == 'field' or resposta == 'f' or resposta == 'any craps' or resposta == 'ac' or resposta == 'twelve' or resposta == 't' or resposta == 'x':
                        break
                    else:
                        print('?')
            
            if fase == 2:   #opcoes de aposta na fase point
                print('\nQual? (Field(f) / Any Craps(ac) / Twelve(t) / Não quero mais apostar(x))')
                while 1:
                    resposta = input()
                    resposta = resposta.lower()
                    if resposta == 'field' or resposta == 'f' or resposta == 'any craps' or resposta == 'ac' or resposta == 'twelve' or resposta == 't' or resposta == 'x':
                        break
                    else:
                        print('?')
                
            if resposta != 'x': #se a opcao for uma aposta, input de quanto vai ser apostado
                print('\nQuanto você gostaria de apostar?')
                while 1:
                    aposta = inputInteiro()
                    if aposta > banco:
                        print('\nVocê não tem ' + str(aposta) + ' fichas!')
                    else:
                        banco -= aposta
                        break
                
                if resposta == 'pass line bet' or resposta == 'plb':    #guarda a quantidade de fichas apostadas na variavel da aposta em que ela foi feita
                    plb += aposta
                elif resposta == 'field' or resposta == 'f':
                    f += aposta
                elif resposta == 'any craps' or resposta == 'ac':
                    ac += aposta
                elif resposta == 'twelve' or resposta == 't':
                    t += aposta
                
                if plb + f + ac + t > 0:    #se vc tiver alguma aposta, mostrar as apostas que vc tem
                    print('\n-------- Suas Aposta --------\n')
                    if plb > 0:
                        print(str(plb) + ' fichas no Pass Line Bat')
                    if f > 0:
                        print(str(f) + ' fichas no Fields')
                    if ac > 0:
                        print(str(ac) + ' fichas no Any Crap')
                    if t > 0:
                        print(str(t) + ' fichas no Twelve')
                    print('\n-----------------------------')
                
                print('\nVocê tem ' + str(banco) + ' fichas')   #mostrar quantas fichas vc tem
                print('\nGostaria de fazer mais alguma aposta? (s/n)')
            else:
                print('\nGostaria de fazer alguma aposta? (s/n)')
    
    if plb + f + ac + t == 0:    #se nenhuma aposta tiver sido feita até sair do loop de apostas, o jogo se encerra
        break
    
    print('\nOs dados serão lançados!') #lancamento dos dados
    
    dadoA = random.randint(1,6)
    dadoB = random.randint(1,6)
    soma = dadoA + dadoB
    
    printDados()
    
    if plb > 0: #resultado do plb
        if fase == 1:
            if soma == 7 or soma == 11:
                print('Você ganhou ' + str(plb) + ' fichas com a aposta no Pass Line Bat!')
                banco += plb * 2
                plb = 0
            elif soma == 2 or soma == 3 or soma == 12:
                print('Você perdeu suas ' + str(plb) + ' fichas apostadas no Pass Line Bat!')
                plb = 0
            elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                print('Sua aposta de ' + str(plb) + ' fichas no Pass Line Bat vai para o Point!')
                somaplb = soma
                fase = 2
        elif fase == 2:
            if soma == somaplb:
                print('Você ganhou ' + str(plb) + ' fichas com a aposta no Pass Line Bat!')
                banco += plb * 2
                plb = 0
                fase = 1
            elif soma == 7:
                print('Você perdeu suas ' + str(plb) + ' fichas apostadas no Pass Line Bat!')
                plb = 0
                fase = 1
            else:
                print('Sua aposta de ' + str(plb) + ' fichas no Pass Line Bat continua no Point')
    
    if f > 0: #resultado do f
        if soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
            print('Você ganhou ' + str(f) + ' fichas com a aposta no Field!')
            banco += f * 2
        elif soma == 5 or soma == 6 or soma == 7 or soma == 8:
            print('Você perdeu suas ' + str(f) + ' fichas apostadas no Field!')
        elif soma == 2:
            print('Você ganhou ' + str(f * 2) + ' fichas com a aposta no Field!')
            banco += f * 3
        elif soma == 12:
            print('Você ganhou ' + str(f * 3) + ' fichas com a aposta no Field!')
            banco += f * 4
        f = 0
    
    if ac > 0:  #resultado do ac
        if soma == 2 or soma == 3 or soma == 12:
            print('Você ganhou ' + str(ac * 7) + ' fichas com a aposta no Any Craps!')
            banco += ac * 8
        else:
            print('Você perdeu suas ' + str(ac) + ' fichas apostadas no Any Craps!')    
        ac = 0
        
    if t > 0:  #resultado do t
        if soma == 12:
            print('Você ganhou ' + str(t * 30) + ' fichas com a aposta no Twelve!')
            banco += t * 31
        else:
            print('Você perdeu suas ' + str(t) + ' fichas apostadas no Twelve!')    
        t = 0
    
    print('\nVocê tem ' + str(banco) + ' fichas') #mostra quantas fichas vc tem
    if banco == 0 and plb == 0:
        print('...e por isso você será expulso do SUPER CRAPS DO ARANHA')
        break

if banco == 0:
    print('\n>>> GAME OVER <<<')
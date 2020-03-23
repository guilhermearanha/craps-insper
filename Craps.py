#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:26:42 2020

@author: guilhermearanha
"""

print('Bem vindo ao SUPER CRAPS DO ARANHA')

while 1:
    try:
        banco = int(input('Quantas fichas você tem?\n\n'))
        break
    except:
        print('Um número inteiro, por favor...\n')

while banco > 0:
    print('∆ Está iniciado o Come Out ∆')
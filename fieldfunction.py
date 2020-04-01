# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:32:26 2020

@author: Lucas Kang
"""
def field(num_bet_field,soma_dos_dados,num_fichas):
    if soma_dos_dados in [3,4,9,10,11]:
        num_fichas += num_bet_field
        print (num_fichas)
    if soma_dos_dados == 2:
        num_fichas += (2*num_bet_field)
        print (num_fichas)
    elif soma_dos_dados == 12:
        num_fichas += (3*num_bet_field)
        print (num_fichas)
    if soma_dos_dados in [5,6,7,8]:
        num_fichas -= num_bet_field
        print(num_fichas)
    return num_fichas

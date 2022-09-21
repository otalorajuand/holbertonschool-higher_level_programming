#!/usr/bin/python3                                                                                                                              
import hidden_4                                                                                                                                 
                                                                                                                                                
lista = dir(hidden_4)                                                                                                                           
                                                                                                                                                
for elem in lista:                                                                                                                              
        if elem[0] != "_":                                                                                                                      
                print("{}".format(elem)) 


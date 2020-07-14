#!python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:19:36 2020

@author: victor.bertoldo
"""

# x = 3
# y = 2

# print(x + y)

# del x

#print(x)

def testeFunc(a, b):
    return a * b

print(testeFunc(3, 5))

def adicionaNumeros(x, y, z=None, *args):    
    if(z is None):
        return x + y
    else:
        return x + y + z
    
print(adicionaNumeros(1, 2))    
print(adicionaNumeros(1,2,3))

f = adicionaNumeros
print(f(1,2))


# tupla
a = (1, 2, 3, 4, 5, 5)
print(a)
    
    
# lista
b = list('abcd')
print(b)    
b.append(True)
print(b)

for i in a:
    print(i*2)
    
i = 0
while(i != len(b)):
    print("Item " + str(i) + ' é '  + str(b[i]))
    i += 1

print("\n")    
   
nome = "Victor Bertoldo"
print(nome[0])
print(nome[-1])
print(nome[1:3])

sobrenome = nome.split(" ")[1]
print(sobrenome)
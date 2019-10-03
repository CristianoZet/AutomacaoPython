from random import randint


lista = []
i = 0 
while(i < 8):
    numero = randint(0,9) 
    lista.append(numero)
    i = i  + 1 

aux = str(lista).strip('[]')
aux.strip(',')

print(aux.strip(','))    




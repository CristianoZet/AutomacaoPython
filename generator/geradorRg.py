from random import randint


lista = []
aux = ''
i = 0 
while(i < 8):
    numero = randint(0,9) 
    lista.append(numero)
    aux = aux + str(numero)
    i = i  + 1 
print (aux)






from random import randint
import datetime

data = datetime.datetime.now()

bissexto = False
dataValida = False
dia = randint(1,31)
mes = randint(1,12)
ano = randint(1900,(data.year - 18))
dataGerada = ''

while (dataValida == False):
    #Valida se é ano bissexto
    if (ano % 4) == 0:
        if(ano % 100) != 0:
            bissexto = True
        elif(ano % 400) == 0:
            bissexto = True
    else:
        bissexto = False

    #Validação dos meses
    if mes == 2:
        if bissexto == True:
            if dia <= 29:
                dataValida = True
        elif bissexto == False:
            if dia <= 28:
                dataValida = True
            else:
                dataValida = False

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            dataValida = True
        else:
            dataValida = False

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        if dia <= 30:
            dataValida = True
        else:
            dataValida = False

    #Ajusta o retorno para preenchimento
    if dia < 10:
        dataGerada = '0{}0{}{}'.format(dia, mes, ano)
    else:
        dataGerada = '{}0{}{}'.format(dia, mes, ano)
print(dataGerada)

# parte 2, gerar pegar o valor e formatar

if len(dataGerada) <= 8:
	dataGerada = '{}/{}/{}'.format(dataGerada[:2], dataGerada[2:4], dataGerada[4:8])
else:
	dataGerada = '01/01/1900'	

print(dataGerada)



    




############################################################################
#Nome: Gerador de CPF (com regra válida)
#Data: 08/10/2019
#Versão: 1.0
#Autor(a): Francielle Consoni
############################################################################

#Importando as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from random import randint

#Declaração de Variáveis
CONTADOR = 0
CPF = [0,0,0,0,0,0,0,0,0,0,0]
DIGITO1 = 0
DIGITO2 = 0

print("***GERADOR DE CPFs VÁLIDOS***\n\n")
#Gerando os 9 primeiros dígitos
while (CONTADOR < 9):
    CPF [CONTADOR]= randint(0,9)
    CONTADOR = CONTADOR + 1

#Aplicando a regra para a geração do primeiro dígito verificador
DIGITO1 = CPF[0]*10 + CPF[1]*9 + CPF[2]*8 + CPF[3]*7 + CPF[4]*6 + CPF[5]*5 + CPF[6]*4 + CPF[7]*3 + CPF[8]*2
RESTO = DIGITO1 % 11
if ((RESTO == 0) or (RESTO == 1)):
    DIGITO1 = 0
else:
    DIGITO1 = 11 - RESTO
CPF[CONTADOR] = DIGITO1

#Aplicando a regra para a geração do segundo dígito verificador
DIGITO2 = CPF[0]*11 + CPF[1]*10 + CPF[2]*9 + CPF[3]*8 + CPF[4]*7 + CPF[5]*6 + CPF[6]*5 + CPF[7]*4 + CPF[8]*3 + CPF[9]*2
RESTO2 = DIGITO2 % 11
if ((RESTO2 == 0) or (RESTO2 == 1)):
    DIGITO2 = 0
else:
    DIGITO2 = 11 - RESTO2
CPF[CONTADOR+1] = DIGITO2

#Imprimindo corretamente sem máscara
CONTADOR = 0
CPF_SEM_MASCARA = ' '
while (CONTADOR < 11):
    CPF_SEM_MASCARA = CPF_SEM_MASCARA + str(CPF[CONTADOR])
    CONTADOR = CONTADOR + 1
print("Sem Máscara:",CPF_SEM_MASCARA)

#Imprimindo corretamente com máscara
CONTADOR = 0
CPF_COM_MASCARA = ' '
while (CONTADOR < 11):
    CPF_COM_MASCARA = CPF_COM_MASCARA + str(CPF[CONTADOR])
    if (CONTADOR == 2 or CONTADOR == 5):
        CPF_COM_MASCARA = CPF_COM_MASCARA + '.'
    if (CONTADOR == 8):
        CPF_COM_MASCARA = CPF_COM_MASCARA + '-'
    CONTADOR = CONTADOR + 1
print("Com Máscara:",CPF_COM_MASCARA)

input()








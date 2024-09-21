from usuario import *
from login import *
import os
import datetime
import csv

# Dados do Usuário
usuario_nome = pegar_nome(input('Nome completo: '))
usuario_nascimento = pegar_nascimento(input('Data de nascimento [dd/mm/aaaa]: '))
user_name = usuario_nome[0]
nascimento = usuario_nascimento[0]

# Mensagem de Aniversário
dia = datetime.date.today().day
mes = datetime.date.today().month
if nascimento[1] == dia and nascimento[2] == mes:
    print('Feliz Aniversário!')

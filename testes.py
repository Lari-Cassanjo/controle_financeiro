from usuario import *
from login import *
import pandas as pd
import os
import datetime
import csv

# # Dados do Usuário
# usuario_nome = pegar_nome(input('Nome completo: '))
# usuario_nascimento = pegar_nascimento(input('Data de nascimento [dd/mm/aaaa]: '))
# user_name = usuario_nome[0]
# nascimento = usuario_nascimento[0]

# # Mensagem de Aniversário
# dia = datetime.date.today().day
# mes = datetime.date.today().month
# if nascimento[1] == dia and nascimento[2] == mes:
#     print('Feliz Aniversário!')

class Dados:
    arquivo_financeiro = 'financeiro.csv'
    
    @classmethod
    def iniciar_arquivo():
        pass

def inserir_dados(data='', valor=0.0, tipo='Saída', descricao=''):
    with open('financeiro.csv', 'w',newline='',encoding='utf-8') as arquivo_financeiro:
        fieldnames = ['data','valor','tipo','descricao']
        writer = csv.DictWriter(arquivo_financeiro, fieldnames=fieldnames)
        writer.writeheader()
        dado = {
            'data': data,
            'valor': valor,
            'tipo': tipo,
            'descricao': descricao
        }
        writer.writerow(dado)

d1 = inserir_dados('21/09/2024',233.45,'Saída','Farmácia')
d2 = inserir_dados('09/08/2024',75.02,'Saída','Mercado')
d3 = inserir_dados('11/09/2024',109.90,'Entrada','Projeto Josh')
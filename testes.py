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
    ARQUIVO_FINANCEIRO = 'financeiro.csv'
    COLUNAS = ['data','valor','tipo','descricao']
    
    
    @classmethod
    def iniciar_arquivo(cls):
        try:
            pd.read_csv(cls.ARQUIVO_FINANCEIRO)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUNAS)
            df.to_csv(cls.ARQUIVO_FINANCEIRO, index=False)
    
    @classmethod
    def add_entrada(cls, data, valor, tipo, descricao):
        dado = {
            'data': data,
            'valor': valor,
            'tipo': tipo,
            'descricao': descricao
        }
        with open(cls.ARQUIVO_FINANCEIRO, 'a',newline='',encoding='utf-8') as arquivocsv:
            writer = csv.DictWriter(arquivocsv, fieldnames=cls.COLUNAS)
            writer.writerow(dado)
        print('Entrada adicionada com sucesso!')
        
            
Dados.iniciar_arquivo()
Dados.add_entrada('21/09/2024',233.45,'Saída','Farmácia')
Dados.add_entrada('09/08/2024',75.02,'Saída','Mercado')
Dados.add_entrada('11/09/2024',109.90,'Entrada','Projeto Josh')

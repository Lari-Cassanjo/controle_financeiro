from usuario import *
from login import *
from inserir_transacoes import *
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
    def add_transacao(cls, data, valor, tipo, descricao):
        nova_transacao = {
            'data': data,
            'valor': valor,
            'tipo': tipo,
            'descricao': descricao
        }
        with open(cls.ARQUIVO_FINANCEIRO, 'a',newline='',encoding='utf-8') as arquivocsv:
            writer = csv.DictWriter(arquivocsv, fieldnames=cls.COLUNAS)
            writer.writerow(nova_transacao)
        print('Entrada adicionada com sucesso!')
        
def add():
    Dados.iniciar_arquivo()
    data = inserir_data('Insira a data da transação [dd/mm/aaaa] ou pressione ENTER para inserir a data de hoje: ', allow_default=True)
    valor = inserir_valor()
    tipo = inserir_tipo()
    descricao = inserir_descricao()
    Dados.add_transacao(data, valor, tipo, descricao)
            
add()

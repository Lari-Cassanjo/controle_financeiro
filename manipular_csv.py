from inserir_transacoes import *
import pandas as pd
from datetime import datetime
import csv

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
        
    @classmethod
    def ler_transacoes(cls, inicio, fim):
        df = pd.read_csv(cls.ARQUIVO_FINANCEIRO)
        df['data'] = pd.to_datetime(df['data'], format=formato_data)
        inicio = datetime.strptime(inicio, formato_data)
        fim = datetime.strptime(fim, formato_data)
        
        filtro = (df['data'] >= inicio) & (df['data'] <= fim)
        df_filtrado = df.loc[filtro]
        
        if df_filtrado.empty:
            print('Nenhuma transação encontrada no tempo selecionado!')
        else:
            print(f'Transações de {inicio.strftime(formato_data)} até {fim.strftime(formato_data)}')
            print(df_filtrado.to_string(index=False, formatters={'data': lambda x: x.strftime(formato_data)}))
        
            entradas_totais = df_filtrado[df_filtrado['tipo'] == 'Entrada']['valor'].sum()
            retiradas_totais = df_filtrado[df_filtrado['tipo'] == 'Retirada']['valor'].sum()
            print('\nResumo:')
            print(f'Total de Entradas: R${entradas_totais:.2f}')
            print(f'Total de Entradas: R${retiradas_totais:.2f}')
            print(f'Saldo: R${(entradas_totais - retiradas_totais):.2f}')
        
        return df_filtrado
        
def add():
    Dados.iniciar_arquivo()
    data = inserir_data('Insira a data da transação [dd/mm/aaaa] ou pressione ENTER para inserir a data de hoje: ', allow_default=True)
    valor = inserir_valor()
    tipo = inserir_tipo()
    descricao = inserir_descricao()
    Dados.add_transacao(data, valor, tipo, descricao)
    
def menu():
    while True:
        print('\n1 - Nova transação')
        print('2 - Ver transações e resumo filtrados por data')
        print('3 - Sair')
        selecao = int(input('Digite sua escolha: '))
        
        if selecao == 1:
            add()
        elif selecao == 2:
            inicio = inserir_data('Insira uma data de início (dd/mm/aaaa): ')
            fim = inserir_data('Insira uma data de fim (dd/mm/aaaa): ')
            df = Dados.ler_transacoes(inicio,fim)
        elif selecao == 3:
            print('Fechando programa...')
            break
        else:
            print('Escolha inválida! Digite 1, 2 ou 3.')

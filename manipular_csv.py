from inserir_transacoes import *
import pandas as pd
from datetime import datetime
import csv

class Dados:
    ARQUIVO_FINANCEIRO = 'financeiro.csv'
    COLUNAS = ['data','valor','tipo','descricao']
    
    @classmethod
    # iniciar ou criar arquivo financeiro (csv com pandas)
    def iniciar_arquivo(cls):
        try:
            pd.read_csv(cls.ARQUIVO_FINANCEIRO)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUNAS)
            df.to_csv(cls.ARQUIVO_FINANCEIRO, index=False)
    
    @classmethod
    # Função para adicionar transações
    def add_transacao(cls, data, valor, tipo, descricao):
        # Dicionário com os dados necessários para inserir uma transição
        nova_transacao = {
            'data': data,
            'valor': valor,
            'tipo': tipo,
            'descricao': descricao
        }
        # Abrindo arquivo no modo 'append'
        with open(cls.ARQUIVO_FINANCEIRO, 'a',newline='',encoding='utf-8') as arquivocsv:
            # Definindo o cabeçalho e inserindo dados
            writer = csv.DictWriter(arquivocsv, fieldnames=cls.COLUNAS)
            writer.writerow(nova_transacao)
        print('Entrada adicionada com sucesso!')
        
    @classmethod
    # Função para ler os dados do arquivo financeiro
    def ler_transacoes(cls, inicio, fim):
        # Iniciando um dataframe
        df = pd.read_csv(cls.ARQUIVO_FINANCEIRO)
        # Selecionando a coluna 'data' e definindo a formatação dos dados
        df['data'] = pd.to_datetime(df['data'], format=formato_data) # Transformando data em objeto datetime
        # Obtendo datas de início e fim para filtrar os dados
        inicio = datetime.strptime(inicio, formato_data) # Transformando objeto datetime em string
        fim = datetime.strptime(fim, formato_data)
        
        # Configurando o filtro e criando uma máscara para ler o arquivo
        filtro = (df['data'] >= inicio) & (df['data'] <= fim)
        df_filtrado = df.loc[filtro]
        
        # Verificando se há transações entre as datas do filtro
        if df_filtrado.empty:
            print('Nenhuma transação encontrada no tempo selecionado!')
        else:
            print(f'Transações de {inicio.strftime(formato_data)} até {fim.strftime(formato_data)}') # Formatando a data
            print(df_filtrado.to_string(index=False, formatters={'data': lambda x: x.strftime(formato_data)})) # Transformando data para string

            # Obtendo e somando entradas e retiradas para gerar um resumo e saldo final
            entradas_totais = df_filtrado[df_filtrado['tipo'] == 'Entrada']['valor'].sum()
            retiradas_totais = df_filtrado[df_filtrado['tipo'] == 'Retirada']['valor'].sum()
            print('\nResumo:')
            print(f'Total de Entradas: R${entradas_totais:.2f}')
            print(f'Total de Entradas: R${retiradas_totais:.2f}')
            print(f'Saldo: R${(entradas_totais - retiradas_totais):.2f}')
        
        return df_filtrado

# Função para adicionar uma transação usando a classe Dados
def add():
    Dados.iniciar_arquivo()
    data = inserir_data('Insira a data da transação [dd/mm/aaaa] ou pressione ENTER para inserir a data de hoje: ', allow_default=True)
    valor = inserir_valor()
    tipo = inserir_tipo()
    descricao = inserir_descricao()
    Dados.add_transacao(data, valor, tipo, descricao)

# Função para criar um menu e dar opções de ações
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

from usuario import *
import os

# Função de Login
def login():
    arquivo_usuario = 'dados_usuario.txt'
    # verificando se o arquivo do usuário existe
    if os.path.exists(arquivo_usuario):
        primeiro_acesso = False
    else:
        primeiro_acesso = True

    # Caso não exista, trata como primeiro acesso
    if primeiro_acesso:
        print(f'{'Inscrição':^30}')
        print('-'*30)
        # Cria o arquivo do usuário e abre ele no modo 'append'
        arquivo_usuario = open('dados_usuario.txt', 'a')
        # Obtém os dados do usuário com as funções do arquivo usuario.py
        usuario_nome = pegar_nome(input('Nome completo: '))
        usuario_nascimento = pegar_nascimento(input('Data de nascimento [dd/mm/aaaa]: '))
        # Obtém uma senha criada pelo usuário
        usuario_senha = input('Senha: ')
        # Escrevendo os dados obtidos no arquivo do usuário
        arquivo_usuario.write(f'{usuario_nome[1]}\n')
        arquivo_usuario.write(f'{usuario_nascimento[0]}\n')
        arquivo_usuario.write(usuario_senha)
        print('Usuário adicionado com sucesso!\n')
    # Caso exista, inicia o login
    else:
        print(f'{'LOGIN':^30}')
        print('-'*30)
        # Abre o arquivo no modo 'read'
        arquivo_usuario = open('dados_usuario.txt', 'r')
        usuario = arquivo_usuario.readlines()
        # Recupera os dados do usuário do arquivo
        usuario_nome = pegar_nome(usuario[0].strip())
        usuario_nascimento = pegar_nascimento(usuario[1].strip())
        usuario_senha = usuario[2]
        # Pede os dados para o login
        nome = input('Nome: ')
        senha = input('Senha: ')
        # Confere o login
        if nome == usuario_nome[0] and senha == usuario_senha:
            print(f'Login efetuado com sucesso!\n')
        else:
            print('Usuário e/ou senha inválidos!')
    
    return usuario_nome, usuario_nascimento

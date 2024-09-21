from usuario import *
import os

def login():
    arquivo_usuario = 'dados_usuario.txt'
    if os.path.exists(arquivo_usuario):
        primeiro_acesso = False
    else:
        primeiro_acesso = True

    if primeiro_acesso:
        print(f'{'Inscrição':^30}')
        print('-'*30)
        arquivo_usuario = open('dados_usuario.txt', 'a')
        usuario_nome = pegar_nome(input('Nome completo: '))
        usuario_nascimento = pegar_nascimento(input('Data de nascimento [dd/mm/aaaa]: '))
        usuario_senha = input('Senha: ')
        arquivo_usuario.write(f'{usuario_nome[1]}\n')
        arquivo_usuario.write(f'{usuario_nascimento[0]}\n')
        arquivo_usuario.write(usuario_senha)
        print('Usuário adicionado com sucesso!\n')
    else:
        print(f'{'LOGIN':^30}')
        print('-'*30)
        arquivo_usuario = open('dados_usuario.txt', 'r')
        usuario = arquivo_usuario.readlines()
        usuario_nome = pegar_nome(usuario[0].strip())
        usuario_nascimento = pegar_nascimento(usuario[1].strip())
        usuario_senha = usuario[2]
        nome = input('Nome: ')
        senha = input('Senha: ')
        if nome == usuario_nome[0] and senha == usuario_senha:
            print(f'Login efetuado com sucesso!\n')
        else:
            print('Usuário e/ou senha inválidos!')
    
    return usuario_nome, usuario_nascimento

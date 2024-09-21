# Dados do usuário: nome, nascimento

def pegar_nome(add_nome):
    nome_completo = add_nome
    nome = nome_completo.split(' ')
    nome = nome[0]
    
    return nome, nome_completo

def pegar_nascimento(nascimento):
    nascimento = nascimento
    data = nascimento.split('/')
    dia = int(data[0])
    mes = int(data[1])
    return nascimento, dia, mes

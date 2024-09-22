# Função para obter o nome completo e o primeiro nome do usuário
def pegar_nome(add_nome):
    nome_completo = add_nome
    nome = nome_completo.split(' ')
    nome = nome[0]
    
    return nome, nome_completo

# Função para obter a data de nascimento do usuário
def pegar_nascimento(nascimento):
    nascimento = nascimento
    data = nascimento.split('/')
    dia = int(data[0])
    mes = int(data[1])
    return nascimento, dia, mes

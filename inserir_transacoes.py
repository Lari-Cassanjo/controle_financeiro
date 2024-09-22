from datetime import datetime

formato_data = '%d/%m/%Y'
CATEGORIAS = {'E': 'Entrada', 'R': 'Retirada'}

# Função para inserir e validar data
def inserir_data(prompt, allow_default=False):
    # Obter a data em forma de string
    data_str = input(prompt)
    # Caso não insira data e for permitido default, retorna a data atual
    if allow_default and not data_str:
        return datetime.today().strftime(formato_data)
    
    # Validando a data
    try:
        # Tenta transformar a string data em objeto datetime
        data_valida = datetime.strptime(data_str, formato_data)
        return data_valida.strftime(formato_data)
    except ValueError:
        print('Formato de data inválido! Por favor, insira uma data no formato [dd/mm/aaaa].')
        return inserir_data(prompt, allow_default)

# Função para inserir valor
def inserir_valor():
    try:
        valor = float(input('Insira o valor: R$'))
        # Se certificando de que será um valor positivo e maior que 0
        if valor <= 0:
            raise ValueError('Valor deve ser maior que 0!')
        return valor
    except ValueError as e:
        print(e)
        return inserir_valor()

# Função para inserir o tipo da transição
def inserir_tipo():
    tipo = input("Defina o tipo de transação ['E' para Entrada e 'R' para Retirada]: ").upper()
    # Verificando se a resposta é válida
    if tipo in CATEGORIAS:
        return CATEGORIAS[tipo]
    
    print("Tipo inválido! Digite 'E' para Entrada e 'R' para Retirada.")
    return inserir_tipo()

# Função para inserir a descrição
def inserir_descricao():
    return input('Insira uma descrição (opcional): ')

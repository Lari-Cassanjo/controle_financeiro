from datetime import datetime

formato_data = '%d/%m/%Y'
CATEGORIAS = {'E': 'Entrada', 'R': 'Retirada'}

def inserir_data(prompt, allow_default=False):
    data_str = input(prompt)
    if allow_default and not data_str:
        return datetime.today().strftime(formato_data)
    
    try:
        data_valida = datetime.strptime(data_str, formato_data)
        return data_valida.strftime(formato_data)
    except ValueError:
        print('Formato de data inválido! Por favor, insira uma data no formato [dd/mm/aaaa].')
        return inserir_data(prompt, allow_default)

def inserir_valor():
    try:
        valor = float(input('Insira o valor: R$'))
        if valor <= 0:
            raise ValueError('Valor deve ser maior que 0!')
        return valor
    except ValueError as e:
        print(e)
        return inserir_valor()

def inserir_tipo():
    tipo = input("Defina o tipo de transação ['E' para Entrada e 'R' para Retirada]: ").upper()
    if tipo in CATEGORIAS:
        return CATEGORIAS[tipo]
    
    print("Tipo inválido! Digite 'E' para Entrada e 'R' para Retirada.")
    return inserir_tipo()

def inserir_descricao():
    return input('Insira uma descrição (opcional): ')

from usuario import *
from login import *
from manipular_csv import *
import datetime

# Dados do Usuário
user_name, nascimento = login()
print(f'Olá, {user_name[0]}! Você nasceu em {nascimento[0]}')

# Mensagem de Aniversário
dia = datetime.date.today().day
mes = datetime.date.today().month
if nascimento[1] == dia and nascimento[2] == mes:
    print('Feliz Aniversário!')

# Menu de Ações
menu()

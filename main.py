from usuario import *
from login import *
from manipular_csv import *
import datetime

# Login (ou Registro) e Boas Vindas!
user_name, nascimento = login()
hora = datetime.now().time()
hora = hora.strftime('%H')
hora = int(hora)

if hora >= 6 and hora < 12:
    cumprimento = 'Bom dia'
elif hora >= 12 and hora < 18:
    cumprimento = 'Boa tarde' 
elif hora >=18 and hora < 23:
    cumprimento = 'Boa noite'
else:
    cumprimento = 'Já está tarde'

print(f'Olá, {user_name[0]}! {cumprimento}.')

# Mensagem de Aniversário
dia = datetime.date.today().day
mes = datetime.date.today().month
if nascimento[1] == dia and nascimento[2] == mes:
    print('Feliz Aniversário!')

# Menu de Ações
menu()

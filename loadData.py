# Lee un archivo JSON para cada una de las tablas
# Inserta los registros
# Utilizamos 'rb' para leer correctamente los caracteres 
# especiales

import json
from models import Clients, Banks, Accounts

def loadClients():
  with open('clients.json', 'rb') as file: 
    data = json.load(file)

    for client in data['clients']:
      cl = Clients()
      cl.id = client['id']
      cl.name = client['name']
      cl.taxNumber = client['taxNumber']
      cl.save()


def loadBanks():
  with open('banks.json', 'rb') as file: 
    data = json.load(file)

    for bank in data['banks']:
      bk = Banks()
      bk.id = bank['id']
      bk.name = bank['name']
      bk.save()


def loadAccounts():
  with open('accounts.json', 'rb') as file: 
    data = json.load(file)

    for account in data['accounts']:
      ac = Accounts()
      ac.clientId = account['clientId']
      ac.bankId = account['bankId']
      ac.balance = account['balance']
      ac.save()

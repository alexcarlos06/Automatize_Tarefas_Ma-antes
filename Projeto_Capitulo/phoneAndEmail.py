#! python3
# phoneAndEmail.py – Encontra números de telefone e endereços de email no clipboard.

import re
import pyperclip
import os

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # Código de área
    (\s|-|\.)? # Separador
    (\d{3}) # Primeiros 3 digitos
    (\s|-|\.) # Separador
    (\d{4}) # Últimos 4 digitos
    (\s*(ext|x|ext.)\s*(\d{2, 5}))? # Extensão
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # Nome de Usuário
    @ # Procura por @
    [a-zA-Z0-9.-]+ # Nome do dominio
    (\.[a-zA-Z]{2,4}) # Ponto seguido de 2 a 4 caracteres   
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email adresses found!')
os.system('PAUSE')

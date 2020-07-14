# Programa para detectar se uma senha é robusta

import re

regex = re.compile(r'''
    (?=.+\d) # Senha deve conter ao menos um digito
    (?=[A-Z]+[a-z]+[0-9]+) # Senha deve conter no minimo uma Letra Maiuscula, uma minuscula e um digito 
    ([^\s]) # Verifica se a senha não possui espaços
    {8,} # Verifica se a senha possui 8 ou mais caracteres
    ''', re.VERBOSE)

password = input('Informe a senha a ser verificada')
if regex.search(password):
    print('Senha Ok')
else:
    print('Favor inserir uma senha mais forte')

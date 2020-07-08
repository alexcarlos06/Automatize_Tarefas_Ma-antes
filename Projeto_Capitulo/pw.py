#! python3
# pw.py – Um programa para repositório de senhas que NÃO É SEGURO!!!.

import sys
import pyperclip
import os


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
passwords = {'email': 'teste@teste'}

account = sys.argv[1]  # o primeiro argumento da linha de comando é o nome da conta
if sys.argv[1] in passwords:
    pyperclip.copy(passwords[sys.argv[1]])
    print()
    print(f'\nSenha para {sys.argv[1]} copiada para área de transferência')
else:
    print(f'\nNão foi encontrado senha cadastrada para {sys.argv[1]}')
os.system('PAUSE')

# TODO Adicionar o comando para inserir novas contas
# TODO Adicionar criptográfia as senhas e contas salvas
# TODO Salvar os dados em um arquivo json
# TODO Retirar todas as senhas do programa principal e utilizar um arquivo json criptografado

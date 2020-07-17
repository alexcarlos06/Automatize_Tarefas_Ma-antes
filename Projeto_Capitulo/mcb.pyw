#! python3
# mcb.pyw - Salva e carrega padrões de texto no clipboard
# Usage: py.exe mcb.pyw save <palavra-chave> - Salva clipboar a palavra chave
#       py.exe mcb.pyw <palavra-chave> - Carrega palavra chave no clipboard
#       py. exe mcb.pym list - Carrega todas as palavras chave no clipboard

import shelve
import pyperclip
import sys

with shelve.open('mcb') as mcbShelf:
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print('Arquivo salvo com sucesso')
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

# TODO: Incluir metodo para apagar algum dado do arquivo
# TODO: Utilizar a biblioteca argparse
# TODO: Incluir mensagem de Help
# TODO: Mensagem de alerta caso não seja fornecido nenhum argumento na linha de comando

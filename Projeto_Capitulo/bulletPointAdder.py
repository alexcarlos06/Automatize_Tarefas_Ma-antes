#! python3
# bulletPointAdder.py – Acrescenta "*" no início de cada linha de texto do clipboard.
import pyperclip
import os

text = pyperclip.paste()  # Obtendo os dados salvos no clipboard
lines = text.split('\n')  # Separando a string recuperada em uma lista divida pelo caractere "\n"
for i in range(len(lines)):  # Percorre todos os índices da lista "lines" em um loop
    lines[i] = '* ' + lines[i]  # Acrescenta um asterisco em cada string da lista "lines"

text = '\n'.join(lines)  # Transforma a lista em uma string unica e adiciona "\n" para pular as linhas novamente
pyperclip.copy(text)  # Copia a novo texto para área de traansferência
print()
os.system('PAUSE')

# TODO Acrecentar metodo para infromar qual o caractere deve ser adicionado a cada linha da string
# TODO Adicionar metodo para que possa ser vizualizado o que foi copiado no terminal
# TODO Adicionar pesquisa para identificar quais linhas terão o marcador adicionado

import os
import pprint
import shelve

caminho = os.getcwd()
arquivos = ['hello.txt', 'sonnet29.txt']

# Abrindo arquivos em modo de leitura
for arquivo in arquivos:
    with open(os.path.join(caminho, arquivo), 'r') as texto:
        pprint.pprint(texto.readlines())

# Abrindo um arquivo em modo de escrita
with open('bacon.txt', 'w') as folha:
    folha.write('Hello world !\n')

# Salvando variável com o módulo shelve
with shelve.open('mydata') as shelfFile:
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats

# Abrindo arquivo shelve e recuperando dados salvos
with shelve.open('mydata') as shelfFile:
    print('O tipo do arquivo é: ',type(shelfFile))
    print('O conteudo do arquivo é: ', shelfFile['cats'])
    print('As chaves são: ', list(shelfFile.keys()))
    print('Os valores do arquivo são: ', list(shelfFile.values()))

# Salvando variáveis em um arquivo externo com extesão .py
cats = [{
    'name': 'Zophie',
    'desc': 'chubby', }, {
    'name': 'Pooka',
    'desc': 'fluffy',
}]
with open('myCats.py', 'w') as fileObj:
    fileObj.write(f'cats = {pprint.pformat(cats)}\n')

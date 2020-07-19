#! python3
# renameDates.py - Renomeia os nomees de arquivos com formato de data MM-DD-AAAA es
# estilo americano para o formato DD-MM-AAAA em estilo europeu

import shutil # Módulo contendo funções do Shell
import os # Módulo contendo funções do sistema operacional
import re # Módulo para uso de expressões regulares

# Cria uma regex que corresponde aos arquivos com formato de data em estilo americano
datePattern = re.compile(r'''^(.*?)     # Tod o texto antes da data
                        ((0|1)?\d)-     # Um ou dois digitos para o mês
                        ((0|1|2|3)?\d)- # Um ou dois digitos para o dia 
                        ((19|20)\d\d)   # Quatro digitos para o ano
                        (.*?)$          # Tod o texto após a data 
''', re.VERBOSE)
# Percorre os arquivos do diretório de trabalho com um loop
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Ignora os arquivos que não tenham uma data
    if not mo:
        continue

    # Obtém as diferentes partes do arquivo
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Compõe o nome do arquivo em estilo europeu
    euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'

    # Obté os paths absolutos completos dos arquivos
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Renomeia os arquivos
    print(f'Renaming {amerFilename} to {euroFilename}')
    shutil.move(amerFilename, euroFilename)

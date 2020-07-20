#! python3
# backupToZip.py - Copia uma pasta toda e seu conteúdo para um arquivo ZIP cujo nome seja incrementado

import zipfile
import os


def backupToZip (folder):
    # Faz backup de t.odo o conteudo de "Folder" em um arquivo ZIP.
    folder = os.path.abspath(folder)  # Garante que folder é um path absoluto
    # Determina o nome do arquivo que esse código deverá usar de acordo com os arquivos já existentes
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Cria o arquivo zip
    print(f'Creating{zipFilename}')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda a árvore de diretório e compacta os arquivos de cada pasta.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        # Acrescenta a pasta atual ao arquivo ZIP
        backupZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)

        # Acrescenta todos os arquivos dessa pasta ao arquivo ZIP
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # Não faz backup dos arquivos ZIP de backup
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')



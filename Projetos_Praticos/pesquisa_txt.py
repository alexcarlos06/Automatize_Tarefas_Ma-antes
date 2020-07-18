#! python3
# Programa pesquisa termos em um arquivo TXT informado pelo usuário
import re

file_path = r'C:\Users\alexc\Documents\RE0501.txt'
records = []
pattern1 = re.compile(r'(Emitente:\d{1,7}).*(Série:\d{0,3})\s.*(Documento:\s\d{1,7})\s.*\s.*\s.*\s.*\s.*'
                      r'(Estabelecimento:\d{1,3})(.*\s){4}.*(Data Transação:\s\d{2}/\d{2}/\d{4})'
                      r'(.*\s){39}\s*(\s*\d{1,8})*'
                      r'(.*\s){6}\s*(.*\n.*\n.*\n.*\n)')


with open(file_path, 'r') as file:
    reader = file.read()
    for x in pattern1.findall(reader):
        if x[7] == '45110200' or x[7] == '45110300':
            data_temp = ' - '.join([x[0], x[1], x[2], x[3], x[5], x[7], x[9]])
            records.append(data_temp)
pattern2 = re.compile(r'\n')
pattern3 = re.compile(r'\s{2,20}')

with open('Relatório.txt', 'w', encoding='UTF-8') as relatorio:
    for x in records:
        records = pattern2.sub('', x)
        records = pattern3.sub('', records)
        ponteiro = relatorio.write(records)
        relatorio.write('\n')

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # Obtendo o conteudo da url
res.raise_for_status() # Gerando uma exceção caso haja um erro no download da pagina
with open('RomeuAndJuliet.txt', 'wb') as playFile: # Gerandoum arquivo para ser gravado em modo binário
    for chunk in res.iter_content(100000):  # Retorna uma porção do conteudo em bites (100000)
        playFile.write(chunk)  # Escreve o conteudo no arquivo


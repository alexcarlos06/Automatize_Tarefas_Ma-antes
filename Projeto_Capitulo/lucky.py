#! python3
# luck.py - Abre varios resultados de pesquisa no site google.com em abas diferentes

import sys
import webbrowser
import requests
import bs4

pesquisa = 'Python solver'
print('Googling...')  # Exibem a mensgem enquanto faz a pesquisa na pagina do Google
res = requests.get(f'https://google.com/search?q={pesquisa}')


# Obtem os links da pesquisa do google
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.find_all('div', )
for link in links:
    url = link.find('a')
    if url:
        print(url)

# Abre uma aba do navegador para cada item achado
'''numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(f'http://google.com{linkElems[i].get("href")}')
'''
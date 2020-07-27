#! python3
# mapIt.py - Inicia o mapa no navegador usado o endereço da linha de comando ou do clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Obtem o endereço da linha de comando
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open(f'https://www.google.com/maps/place/{address}')

# Corrigindo a ordem da instrução elif evitando ser exibido duas mensagens tomando como base vampire.py

name = input('Enter your name: ')
age = int(input('enter your age: '))

if name == 'Alice':
    print('Hi,	Alice.')
elif age < 12:
    print('You	are	not	Alice,	kiddo.')
elif age > 100:
    print('You	are	not	Alice,	grannie.')
elif age > 2000:
    print('Unlike	you,	Alice	is	not	an	undead,	immortal	vampire.')
# Programa recebe uma lista e transforma em uma strng separada por ',' e and antecedendo o ultimo elemento.

def concatenar(lista):
    temporario = ''
    index = 0
    for item in lista:
        if index == len(lista)-1:
            temporario += f'and {item}.'
        else:
            temporario += f'{item}, '
        index += 1
    return temporario


spam = ['apples', 'bananas', 'tofu', 'cats', 1]
print(concatenar(spam))

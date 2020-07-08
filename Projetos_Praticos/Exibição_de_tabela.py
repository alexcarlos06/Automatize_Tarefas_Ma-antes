# Programa que exibe um lista de listas na tela em formato de tabela


def printTable(array: list):
    columwidth = 0
    itemwidth = 0
    for item in array:
        if len(item) > columwidth:
            columwidth = len(item)
        for register in item:
            if len(register) > itemwidth:
                itemwidth = len(register)

    for item in array:
        if len(item) < columwidth:
            for x in range(columwidth - len(item)):
                item.append('')
        print('_' * (columwidth * (itemwidth + 4)))
        for register in item:
            print('| ', end='')
            print(register.rjust(itemwidth), end='')
            print(' |', end='')
        print()
    print('_' * (columwidth * (itemwidth + 4)))


tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose','teste 1', 'teste 2']]

printTable(tableData)

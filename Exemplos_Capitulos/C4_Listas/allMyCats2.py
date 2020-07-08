#  Exemplo do trabalho do programa allMyCats.py sendo feito com lista


catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 'º (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # concatenação	de	lista
    print('The cat names are: ')
for name in catNames:
    print(' ' + name)

# Montagem de Matriz com o estrutura de repetição, pegar a matrix da variável grid e exibir com a orientação vertical
# adotando a primeira posição da matriz sendo (0, 0) coordenadas x  para direita e coordenadas y aumentam para baixo
# A matriz resultante deve ter um formato aproximado de coração

grid = [['.',	'.',	'.',	'.',	'.',	'.'],
        ['.',	'O',	'O',	'.',	'.',	'.'],
        ['O',	'O',	'O',	'O',	'.',	'.'],
        ['O',	'O',	'O',	'O',	'O',	'.'],
        ['.',	'O',	'O',	'O',	'O',	'O'],
        ['O',	'O',	'O',	'O',	'O',	'.'],
        ['O',	'O',	'O',	'O',	'.',	'.'],
        ['.',	'O',	'O',	'.',	'.',	'.'],
        ['.',	'.',	'.',	'.',	'.',	'.']]

x = 0
y = 0
for item_x in grid[y]:
    for item_y in grid:
        print(grid[y][x], end='')
        y += 1
    x += 1
    y = 0
    print()

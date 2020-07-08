# Programa recebe um dicionário de um inventário de itens e mostra todos os itens, suas quantidades e o total
# Adicionado função addToInventory que adiciona os itens de acordo com uma lista de nomes


def displayInventory(bag_items: dict):
    print('\tThe bag has: ')
    total = 0
    for item, amount in bag_items.items():
        print(f'\t\t{amount:^4}  {str(item).capitalize()}')
        total += amount
    print(f'-' * 40)
    print(f'\tTotal quantity of items {total}\n')


def addToInventory(inventory: dict, addedItems: list):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['dagger', 'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inv)
addToInventory(inv, dragonLoot)
displayInventory(inv)

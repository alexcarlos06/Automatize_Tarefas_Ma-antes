# Exemplo de uso da instrução continue dentro de um laço while

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is	a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
